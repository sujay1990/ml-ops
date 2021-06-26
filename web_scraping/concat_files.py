import pandas as pd
import os
# csv_files = ["rotowire-stats.csv"]


# my_file = open("F:\\Road to Opta\\ml-ops\\stats.txt", "r")
# stats = my_file.read().splitlines()
# my_file.close()
#
# my_file = open("F:\\Road to Opta\\ml-ops\\mid_legends.txt", "r")
# mid_stats = my_file.read().splitlines()
# my_file.close()
#
#
# for i in range(1, 38):
#     csv_files.append("rotowire-stats ({}).csv".format(i))

# result = [x for x in stats if x not in mid_stats]
#
# for i in range(len(result)):
#     result[i] = result[i].upper()
#
#
#
# combined_csv = pd.concat([pd.read_csv(f) for f in csv_files])
# combined_csv.drop(result, axis=1, inplace=True)
# filename = "F:\Road to Opta\player_stats\mid\\2017-2018\\mid_2017_stats.csv"
# combined_csv.to_csv(filename)
# combined_csv = pd.concat([pd.read_csv(f) for f in csv_files])

os.chdir("F:\\Road to Opta\\player_stats\\def")

# def_2016 = pd.read_csv("2016-2017\\def_2016_stats.csv")
# def_2017 = pd.read_csv("2017-2018\\def_2017_stats.csv")
# def_2018 = pd.read_csv("2018-2019\\def_2018_stats.csv")
# def_2019 = pd.read_csv("2019-2020\\def_2019_stats.csv")
# def_2020 = pd.read_csv("2020-2021\\def_2020_stats.csv")
#
# combined_csv = pd.concat([def_2016, def_2017, def_2018, def_2019, def_2020])
# combined_csv.to_csv("def_stats.csv")

def_stats = pd.read_csv("def_stats.csv")
def_stats = def_stats[['Player Name', 'Season', 'Team', 'League', 'OPP', 'H/A', 'Form', 'POS']]

# os.chdir("F:\\Road to Opta\\player_stats\\gk")
# gk_2016 = pd.read_csv("2016-2017\\gk_2016_stats.csv")
# gk_2017 = pd.read_csv("2017-2018\\gk_2017_stats.csv")
# gk_2018 = pd.read_csv("2018-2019\\gk_2018_stats.csv")
# gk_2019 = pd.read_csv("2019-2020\\gk_2019_stats.csv")
# gk_2020 = pd.read_csv("2020-2021\\gk_2020_stats.csv")
#
# combined_csv = pd.concat([gk_2016, gk_2017, gk_2018, gk_2019, gk_2020])
# combined_csv.to_csv("gk_stats.csv")

os.chdir("F:\\Road to Opta\\player_stats\\mid")
#
# mid_2016 = pd.read_csv("2016-2017\\mid_2016_stats.csv")
# mid_2017 = pd.read_csv("2017-2018\\mid_2017_stats.csv")
# mid_2018 = pd.read_csv("2018-2019\\mid_2018_stats.csv")
# mid_2019 = pd.read_csv("2019-2020\\mid_2019_stats.csv")
# mid_2020 = pd.read_csv("2020-2021\\mid_2020_stats.csv")
#
# combined_csv = pd.concat([mid_2016, mid_2017, mid_2018, mid_2019, mid_2020])
# combined_csv.to_csv("mid_stats.csv")

mid_stats = pd.read_csv("mid_stats.csv")
mid_stats = mid_stats[['Player Name', 'Season', 'Team', 'League', 'OPP', 'H/A', 'Form', 'POS']]

#
os.chdir("F:\\Road to Opta\\player_stats\\fw")
#
# fw_2016 = pd.read_csv("2016-2017\\fw_2016_stats.csv")
# fw_2017 = pd.read_csv("2017-2018\\fw_2017_stats.csv")
# fw_2018 = pd.read_csv("2018-2019\\fw_2018_stats.csv")
# fw_2019 = pd.read_csv("2019-2020\\fw_2019_stats.csv")
# fw_2020 = pd.read_csv("2020-2021\\fw_2020_stats.csv")
#
# combined_csv = pd.concat([fw_2016, fw_2017, fw_2018, fw_2019, fw_2020])
# combined_csv.to_csv("fw_stats.csv")

fw_stats = pd.read_csv("fw_stats.csv")
fw_stats = fw_stats[['Player Name', 'Season', 'Team', 'League', 'OPP', 'H/A', 'Form', 'POS']]

combined_csv = pd.concat([def_stats, mid_stats, fw_stats])
# combined_csv.to_csv("fw_stats.csv")

# df_state = pd.read_csv("fw_stats.csv")

Dup_Rows = combined_csv[combined_csv.duplicated()]

print("\n\nDuplicate Rows : \n {}".format(Dup_Rows))

