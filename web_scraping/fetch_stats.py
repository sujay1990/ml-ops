from selenium import webdriver
import os
import time
import pandas as pd
from selenium.webdriver.support.ui import Select
import chromedriver_binary
import urllib.request as urlreq
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

# driver = webdriver.Chrome()
# driver.get("https://www.fotmob.com/livescores/3625830/lineup/montpellier-vs-marseille?date=20210808")
#
#
# driver.find_element_by_xpath('//*[@id="MatchFactsWrapper"]/div/div[2]/div[2]/div[2]/a/button').click()
#
# url = driver.current_url

url = "https://www.fotmob.com/livescores/3625830/lineup/montpellier-vs-marseille?date=20210808"


print(url)

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
print(page_soup)
print("webpage successfully parsed using beautiful soup")

li = page_soup.findAll("li")

print(li)
# //*[@id="MatchFactsWrapper"]/div/div[2]/div[2]/div[3]/a[3]/button

# <div class="css-1fitnu4-StatSectionContainer e1wnrh4f2"><ul class="css-ykt634-StatSection e1wnrh4f1"><li class="css-1yudhro"> Top stats </li><li class="css-1yudhro"><span> FotMob rating</span><span width="28" height="22" class="css-1r1mw9x-PlayerRatingStyled e18zo9eh0">6.4</span></li></ul></div>