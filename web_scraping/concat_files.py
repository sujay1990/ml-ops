import pandas as pd
import os
csv_files = ["rotowire-stats.csv"]


my_file = open("F:\\Road to Opta\\ml-ops\\stats.txt", "r")
stats = my_file.read().splitlines()
my_file.close()

my_file = open("F:\\Road to Opta\\ml-ops\\mid_legends.txt", "r")
mid_stats = my_file.read().splitlines()
my_file.close()


for i in range(1, 38):
    csv_files.append("rotowire-stats ({}).csv".format(i))

os.chdir("F:\Road to Opta\player_stats\mid\\2017-2018")

result = [x for x in stats if x not in mid_stats]

for i in range(len(result)):
    result[i] = result[i].upper()



combined_csv = pd.concat([pd.read_csv(f) for f in csv_files])
combined_csv.drop(result, axis=1, inplace=True)
filename = "F:\Road to Opta\player_stats\mid\\2017-2018\\mid_2017_stats.csv"
combined_csv.to_csv(filename)
combined_csv = pd.concat([pd.read_csv(f) for f in csv_files])

