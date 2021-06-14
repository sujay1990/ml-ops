from selenium import webdriver
import getpass
import os
import time
import pandas as pd
from selenium.webdriver.support.ui import Select
import chromedriver_binary  # Adds chromedriver binary to path
os.chdir("F:\\Road to Opta\\ml-ops")

my_file = open("stats.txt", "r")
stats = my_file.read().splitlines()
my_file.close()

my_file = open("stats_xpath.txt", "r")
xpath = my_file.read().splitlines()
my_file.close()

my_file = open("gk_legends.txt", "r")
gk_stats = my_file.read().splitlines()
my_file.close()

my_file = open("def_legends.txt", "r")
def_stats = my_file.read().splitlines()
my_file.close()

my_file = open("mid_legends.txt", "r")
mid_stats = my_file.read().splitlines()
my_file.close()

my_file = open("fw_legends.txt", "r")
fw_stats = my_file.read().splitlines()
my_file.close()

stats_xpath = dict(zip(stats, xpath))

os.chdir("F:\\Road to Opta\\player_stats")

# Folder names

fw = "fw"
mid = "mid"
defense = "def"
gk = "gk"

if os.path.isdir(defense):
    print(defense, " folder exists")
else:
    os.makedirs(defense, exist_ok=False)

if os.path.isdir(mid):
    print(mid, " folder exists")
else:
    os.makedirs(mid, exist_ok=False)

if os.path.isdir(fw):
    print(fw, " folder exists")
else:
    os.makedirs(fw, exist_ok=False)

if os.path.isdir(gk):
    print(gk, " folder exists")
else:
    os.makedirs(gk, exist_ok=False)

# Choose stats for defensive position


def get_player_stats(pos, pos_stats, ps):

    os.chdir("F:\\Road to Opta\\player_stats\\%s" % str(pos))
    season = range(2016, 2021)
    matchday = range(1, 39)
    position = ps

    for season in season:
        os.chdir("F:\\Road to Opta\\player_stats\\%s" % str(pos))
        if os.path.isdir("%s-%s" % (str(season), str(season + 1))):
            print("folder exists")
            continue
        else:
            os.makedirs("%s-%s" % (str(season), str(season + 1)), exist_ok=False)
        os.chdir("F:\\Road to Opta\\player_stats\\%s\\%s-%s" % (str(pos), str(season), str(season + 1)))
        print("Current working and download directory is", os.getcwd())
        preferences = {
            "profile.default_content_settings.popups": 0,
            "download.default_directory": os.getcwd() + os.path.sep,
            "directory_upgrade": True
        }
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('prefs', preferences)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.rotowire.com/users/login.php?go=%2Fsoccer%2Fstats.php")

        # Enter User name
        print("Enter username:")
        # username = input()
        username = 'sujay1990'
        p = 'barcelona10!!'
        # p = getpass.getpass()
        print("Password entered")

        # send username and password to website

        driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div[1]/form/input[1]").send_keys(username)
        driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div[1]/form/input[2]").send_keys(p)

        # Login in
        driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div[1]/form/button").click()

        while driver.find_element_by_xpath("/html/body/div[1]/div/main/div[1]").text == "Either the username or password was incorrect.":
            print("Enter the right password")
            p = getpass.getpass()
            print("Trying to log in again")
            driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div[1]/form/input[1]").send_keys(username)
            driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div[1]/form/input[2]").send_keys(p)
            driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div[1]/form/button").click()
            if driver.find_element_by_xpath(
                    "/html/body/div[1]/div/main/div[1]").text == "Either the username or password was incorrect.":
                pass
            else:
                print("Login Successful")

        # Choose leagues
        driver.get("https://www.rotowire.com/soccer/stats.php")
        driver.find_element_by_xpath("//*[@id='stats']/div[2]/div[1]/div[1]").click()  # EPL
        driver.find_element_by_xpath("//*[@id='stats']/div[2]/div[1]/div[3]").click()  # UCL
        driver.find_element_by_xpath("//*[@id='stats']/div[2]/div[1]/div[4]").click()  # UEL
        driver.find_element_by_xpath("//*[@id='stats']/div[2]/div[1]/div[5]").click()  # La Liga
        driver.find_element_by_xpath("//*[@id='stats']/div[2]/div[1]/div[6]").click()  # Seria A
        driver.find_element_by_xpath("//*[@id='stats']/div[2]/div[1]/div[7]").click()  # Ligue 1
        driver.find_element_by_xpath("//*[@id='stats']/div[2]/div[1]/div[8]").click()  # Bundesliga
        print(stats_xpath)
        print(pos_stats)
        time.sleep(5.0)
        # Check all the stats for the position

        # for i in stats_xpath:
        #     time.sleep(2.0)
        #     if i in pos_stats:
        #         ids = "//*[@id='%s']" % str(i)
        #         if driver.find_element_by_xpath(str(ids)).is_selected():
        #             pass
        #         else:
        #             time.sleep(2.0)
        #             driver.find_element_by_xpath(stats_xpath.get(i)).click()
        #             print("checking", i)
        #     else:
        #         ids = "//*[@id='%s']" % str(i)
        #         if driver.find_element_by_xpath(str(ids)).is_selected():
        #             time.sleep(2.0)
        #             driver.find_element_by_xpath(stats_xpath.get(i)).click()
        #             print("unchecking", i)

        time.sleep(3.0)
        driver.find_element_by_xpath("//*[@id='playtime']").click()
        time.sleep(2.0)
        driver.find_element_by_xpath("//*[@id='basic']").click()
        time.sleep(2.0)
        driver.find_element_by_xpath("//*[@id='advanced']").click()
        time.sleep(2.0)
        driver.find_element_by_xpath("//*[@id='setpiece']").click()
        time.sleep(2.0)
        driver.find_element_by_xpath("//*[@id='goalie']").click()
        time.sleep(3.0)

        for match_day in matchday:
            driver.find_element_by_xpath("//*[@id='season']").send_keys(season)
            Select(driver.find_element_by_xpath("// *[ @ id = 'position']")).select_by_visible_text(str(position))
            Select(driver.find_element_by_xpath("//*[@id='start']")).select_by_value(str(match_day))
            Select(driver.find_element_by_xpath("//*[@id='end']")).select_by_value(str(match_day))
            driver.find_element_by_xpath("// *[ @ id = 'stats']/div[2]/div[2]/div[5]/button").click()
            time.sleep(15.0)
            driver.find_element_by_xpath("// *[ @ id = 'stats-table']/div[4]/div[2]/button[2]").click()
            time.sleep(5.0)
            print("Downloaded Matchday", match_day)

        csv_files = ["rotowire-stats.csv"]
        for i in range(1, 38):
            csv_files.append("rotowire-stats ({}).csv".format(i))

        for i in range(len(pos_stats)):

            pos_stats[i] = pos_stats[i].upper()

        result = [x for x in stats if x not in pos_stats]

        combined_csv = pd.concat([pd.read_csv(f) for f in csv_files])
        combined_csv.drop(result, axis=1, inplace=True)
        filename = "%s_%s_stat.csv" % (str(pos), str(season))
        combined_csv.to_csv(filename)


get_player_stats(fw, fw_stats, 'F')
