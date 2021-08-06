from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
from operator import itemgetter
import json
import uvicorn
# os.chdir("F:\\Road to Opta\\player_stats\\")

#
app = FastAPI()

mean_stats = pd.read_csv("/usr/src/app/data/scaled_mean_features.csv")
# mean_stats = pd.read_csv("F:\\Road to Opta\\player_stats\\scaled_mean_features.csv")
mean_stats = mean_stats.iloc[:, 1:]


def lowercase(df):
    df['player_name'] = df['player_name'].str.lower()


lowercase(mean_stats)

final_columns = mean_stats.player_name.to_list()


def cosine_similarity_df(x, top, sp, df):
    from sklearn.metrics.pairwise import cosine_similarity
    cosine = cosine_similarity(x.iloc[:, 1:], df.iloc[:, 1:])
    cosine_df = pd.DataFrame(cosine, index=x.iloc[:, 1:].index)
    cosine_df.columns = final_columns
    cosine_df = pd.concat([x.player_name, cosine_df], axis=1)
    cosine_df.set_index('player_name', inplace=True)
    cos_top_10 = cosine_df.sort_values(by=sp, axis=1, ascending=False).iloc[:, 1:top]
    return cos_top_10


def euclid_similarity_df(x, top, sp, df):
    from scipy.spatial.distance import cdist
    euclid = cdist(x.iloc[:, 1:], df.iloc[:, 1:], 'euclid')
    euclid_df = pd.DataFrame(euclid, index=x.iloc[:, 1:].index)
    euclid_df.columns = final_columns
    euclid_df = pd.concat([x.player_name, euclid_df], axis=1)
    euclid_df.set_index('player_name', inplace=True)
    euc_top_10 = euclid_df.sort_values(by=sp, axis=1, ascending=True).iloc[:, 1:top]
    return euc_top_10


def manhattan_similarity_df(x, top, sp, df):
    from scipy.spatial.distance import cdist
    manhattan = cdist(x.iloc[:, 1:], df.iloc[:, 1:], 'cityblock')
    manhattan_df = pd.DataFrame(manhattan, index=x.iloc[:, 1:].index)
    manhattan_df.columns = final_columns
    manhattan_df = pd.concat([x.player_name, manhattan_df], axis=1)
    manhattan_df.set_index('player_name', inplace=True)
    man_top_10 = manhattan_df.sort_values(by=sp, axis=1, ascending=True).iloc[:, 1:top]
    return man_top_10


def minkowski_similarity_df(x, top, sp, df):
    from scipy.spatial.distance import cdist
    minkowski = cdist(x.iloc[:, 1:], df.iloc[:, 1:], 'minkowski')
    minkowski_df = pd.DataFrame(minkowski, index=x.iloc[:, 1:].index)
    minkowski_df.columns = final_columns
    minkowski_df = pd.concat([x.player_name, minkowski_df], axis=1)
    minkowski_df.set_index('player_name', inplace=True)
    mink_top_10 = minkowski_df.sort_values(by=sp, axis=1, ascending=True).iloc[:, 1:top]
    return mink_top_10


def similarity(cos_top_10, euc_top_10, man_top_10, mink_top_10, top):
    import collections
    a_list = cos_top_10.columns.to_list()
    b_list = euc_top_10.columns.to_list()
    c_list = man_top_10.columns.to_list()
    d_list = mink_top_10.columns.to_list()
    comp_list = a_list + b_list + c_list + d_list
    occurrences = collections.Counter(comp_list)
    res = dict(sorted(occurrences.items(), key=itemgetter(1), reverse=True)[:top])
    return res


def getlist(x):
    return list(map(itemgetter(0), x.items()))


class SimilarPlayer(BaseModel):
    player: str
    select_top: int


class SearchPlayer(BaseModel):
    name: str


class ChangeStats(BaseModel):
    list_of_stats: list

@app.post('/similar_players')
async def similar_player(sp: SimilarPlayer):
    similar_df = mean_stats.loc[mean_stats['player_name'] == sp.player.lower()]
    cos_top_10 = cosine_similarity_df(similar_df, sp.select_top, sp.player.lower(), mean_stats)
    euc_top_10 = euclid_similarity_df(similar_df, sp.select_top, sp.player.lower(), mean_stats)
    man_top_10 = manhattan_similarity_df(similar_df, sp.select_top, sp.player.lower(), mean_stats)
    mink_top_10 = minkowski_similarity_df(similar_df, sp.select_top, sp.player.lower(), mean_stats)
    dict_of_players = similarity(cos_top_10, euc_top_10, man_top_10, mink_top_10, sp.select_top)
    final_list = []
    for i in getlist(dict_of_players):
        i = i.title()
        final_list.append(i)
    return {'similar_players': final_list}


@app.post('/search_player_name')
async def search_player(search: SearchPlayer):
    players = mean_stats['player_name'][mean_stats['player_name'].str.contains(search.name.lower())]
    return {f'list of players containing {search.name}': players}


@app.get('/stats_used')
async def stats():
    # with open('F:\\Road to Opta\\ml-ops\\legends.json') as f:
    #         stats = json.load(f)
    # # columns = mean_stats.columns
    return mean_stats.columns.to_list()


@app.get('/legends')
async def stats():
    with open('/usr/src/app/data/legends.json') as f:
            stats = json.load(f)
    return stats


@app.post('/change_stats')
async def stats(change: ChangeStats, sp: SimilarPlayer):
    temp_df = pd.read_csv("/usr/src/app/data/scaled_mean_features.csv")
    temp_df = temp_df.iloc[:, 1:]
    lowercase(temp_df)
    temp_df = temp_df[[*change.list_of_stats]]
    final_columns = temp_df.player_name.to_list()
    similar_df = temp_df.loc[temp_df['player_name'] == sp.player.lower()]
    cos_top_10 = cosine_similarity_df(similar_df, sp.select_top, sp.player.lower(), temp_df)
    euc_top_10 = euclid_similarity_df(similar_df, sp.select_top, sp.player.lower(), temp_df)
    man_top_10 = manhattan_similarity_df(similar_df, sp.select_top, sp.player.lower(), temp_df)
    mink_top_10 = minkowski_similarity_df(similar_df, sp.select_top, sp.player.lower(), temp_df)
    dict_of_players = similarity(cos_top_10, euc_top_10, man_top_10, mink_top_10, sp.select_top)
    final_list = []
    for i in getlist(dict_of_players):
        i = i.title()
        final_list.append(i)
    return {'similar_players': final_list}


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")
