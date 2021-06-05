# Python Football winner prediction Web scraping code

import urllib.request
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

# Function for fetching League table

# epl_table
# laliga_table
# serie_a_table
# bundesliga_table


def league_table(url, filename):

    fotmob_url = url

    req = urllib.request.Request(
        fotmob_url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    uclient = ureq(req)
    page_html = uclient.read()
    uclient.close()

    # get the webpage html in soup format for parsing
    page_soup = soup(page_html, "html.parser")

    # Get all rows from the table
    table_rows = (page_soup.findAll("section", {"class": "css-43vxc8-TableItselfLayout e15qq3az1"}))

    # Fetch all the divs from the table rows

    table_divs = table_rows[0].findAll("div")

    # Each row in the league table has a class attribute. Fetch all the rows with a class attribute and store in a list

    items = range(1, len(table_divs))
    league_rows = []
    for item in items:
        if table_divs[item].has_attr("class"):
            # row_class = table_divs[item]["class"][0] + " " + table_divs[item]["class"][1]
            league_rows.append(table_divs[item])

    table = filename

    f = open(table, "w")
    table_headers = "position, team, games_played, won, draw, lost, goals_scored, goals_conceded, goal_difference, points\n"
    f.write(table_headers)

    for item in range(len(league_rows)):
        team_attr = league_rows[item].findAll("span")
        position = team_attr[0].text
        team = team_attr[1].text
        played = team_attr[2].text
        won = team_attr[3].text
        draw = team_attr[4].text
        lost = team_attr[5].text
        goals_scored = team_attr[6].text.split("-")[0]
        goals_conceded = team_attr[6].text.split("-")[1]
        goal_difference = team_attr[7].text
        points = team_attr[8].text

        f.write(position + "," + team + "," + played + "," + won + "," + draw + "," + lost + "," + goals_scored + "," + goals_conceded + "," + goal_difference + "," + points + "\n")

    f.close()


league_table("https://www.fotmob.com/leagues/54/table/1.-bundesliga", "bundesliga_table.csv")

# epl_table("https://www.fotmob.com/leagues/47/table/premier-league", "epl_table.csv")
# laliga_table("https://www.fotmob.com/leagues/87/table/laliga", "laliga_table.csv")
# serie_a_table("https://www.fotmob.com/leagues/55/table/serie-a", "seria_a_table.csv")
# bundesliga_table("https://www.fotmob.com/leagues/54/table/1.-bundesliga", "bundesliga_table.csv")
