import pandas as pd
import os
import sqlite3

# os.chdir("F:\\Road to Opta\\player_stats\\")
mean_stats = pd.read_csv("scaled_mean_features.csv")
mean_stats = mean_stats.iloc[:, 1:]


def calculate_similarity_df():
    from sklearn.metrics.pairwise import cosine_similarity
    from scipy.spatial.distance import cdist
    cosine = cosine_similarity(mean_stats.iloc[:, 1:])
    euclid = cdist(mean_stats.iloc[:, 1:], mean_stats.iloc[:, 1:], 'euclid')
    manhattan = cdist(mean_stats.iloc[:, 1:], mean_stats.iloc[:, 1:], 'cityblock')
    minkowski = cdist(mean_stats.iloc[:, 1:], mean_stats.iloc[:, 1:], 'minkowski')
    cosine_df = pd.DataFrame(cosine, index=mean_stats.iloc[:, 1:].index)
    cosine_df = pd.concat([mean_stats.player_name, cosine_df], axis=1)
    euclid_df = pd.DataFrame(euclid, index=mean_stats.iloc[:, 1:].index)
    euclid_df = pd.concat([mean_stats.player_name, euclid_df], axis=1)
    manhattan_df = pd.DataFrame(manhattan, index=mean_stats.iloc[:, 1:].index)
    manhattan_df = pd.concat([mean_stats.player_name, manhattan_df], axis=1)
    minkowski_df = pd.DataFrame(minkowski, index=mean_stats.iloc[:, 1:].index)
    minkowski_df = pd.concat([mean_stats.player_name, minkowski_df], axis=1)
    all_players = cosine_df.player_name.to_list()
    cosine_df.columns = ['player_name'] + all_players
    euclid_df.columns = ['player_name'] + all_players
    manhattan_df.columns = ['player_name'] + all_players
    minkowski_df.columns = ['player_name'] + all_players
    return cosine_df, euclid_df, manhattan_df, minkowski_df


calculate_similarity_df()


def similarity(mean_stats, similar_player, cosine_df, euclid_df, manhattan_df, minkowski_df):
    import collections
    from operator import itemgetter

    similar_df = cosine_df.loc[cosine_df['player_name'] == similar_player]
    similar_df.set_index('player_name', inplace=True)
    cos_top_10 = similar_df.sort_values(by=similar_player, axis=1, ascending=False).iloc[:, 1:10]
    similar_df = euclid_df.loc[euclid_df['player_name'] == similar_player]
    similar_df.set_index('player_name', inplace=True)
    euc_top_10 = similar_df.sort_values(by=similar_player, axis=1, ascending=True).iloc[:, 1:10]
    similar_df = manhattan_df.loc[manhattan_df['player_name'] == similar_player]
    similar_df.set_index('player_name', inplace=True)
    man_top_10 = similar_df.sort_values(by=similar_player, axis=1, ascending=True).iloc[:, 1:10]
    similar_df = minkowski_df.loc[minkowski_df['player_name'] == similar_player]
    similar_df.set_index('player_name', inplace=True)
    mink_top_10 = similar_df.sort_values(by=similar_player, axis=1, ascending=True).iloc[:, 1:10]
    a_list = cos_top_10.columns.to_list()
    b_list = euc_top_10.columns.to_list()
    c_list = man_top_10.columns.to_list()
    d_list = mink_top_10.columns.to_list()
    comp_list = a_list + b_list + c_list + d_list
    occurrences = collections.Counter(comp_list)
    res = dict(sorted(occurrences.items(), key=itemgetter(1), reverse=True)[:10])
    return res


os.chdir("F:\\Road to Opta\\player_stats\\")
cnn = sqlite3.connect('game_data.db')
cursor = cnn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("tables existing in game_data db: ", cursor.fetchall())


