import urllib.request as urlreq
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import os

# Change working directory to download files directly into the folder

path_to_folder = "F:\\Road to Opta\\match_results\\"
os.chdir(path_to_folder)
print(" The working directory is set to", path_to_folder)

# URL to download season result

url = "https://www.football-data.co.uk/downloadm.php"

req = urlreq.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

uclient = ureq(req)
page_html = uclient.read()
uclient.close()

# Read HTML using beautiful soup
page_soup = soup(page_html, "html.parser")
print("webpage successfully parsed using beautiful soup")

# Find the tag where download links reside
tr = page_soup.findAll("tr")

# All download links are under 'a' tag under 'tr'

href = []
for i in tr:
    href.append(i.findAll("a"))

# Remove empty entries from the list of 'a' tag

href_filter = list(filter(None, href))

# Retrieve all the links from 'a href' tag

links = []

for link in range(0, len(href_filter)):
    links.append(href_filter[link][0]['href'])

# Find only the relevant links that download .zip folder with csv files

data_zip_links = [link for link in links if "/data.zip" in link]
print("All download links successfully retrieved")

# Create a list of urls to request the files from

website_url = "https://www.football-data.co.uk/"
download_url = []

for i in data_zip_links:
    download_url.append(website_url + i)

# Download the zip file from the website using the above created urls into the working directory
print("Starting zip file download in location", path_to_folder)

for i in download_url:
    zipfile_name = "season_" + i[40:42] + "-" + i[42:44] + ".zip"
    urlreq.urlretrieve(i, zipfile_name)
    print("Finished downloading %s in location %s" % (zipfile_name, path_to_folder))

