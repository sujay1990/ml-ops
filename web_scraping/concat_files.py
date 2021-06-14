import pandas as pd
import os
csv_files = ["rotowire-stats.csv"]

for i in range(1, 38):
    csv_files.append("rotowire-stats ({}).csv".format(i))

os.chdir("F:\Road to Opta\player_stats\def\\2019-2020")

combined_csv = pd.concat([pd.read_csv(f) for f in csv_files])


combined_csv.to_csv("F:\\Road to Opta\\player_stats\\def\\2019-2020\\def_2019_stats.csv")
