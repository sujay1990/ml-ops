from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel

# os.chdir("F:\\Road to Opta\\player_stats\\")

#
app = FastAPI()


mean_stats = pd.read_csv("F:\\Road to Opta\\player_stats\\scaled_mean_features.csv")
mean_stats = mean_stats.iloc[:, 1:]

my_dict = {'player' : 'Messi'}

def cosine_similarity_df():
    from sklearn.metrics.pairwise import cosine_similarity
    cosine = cosine_similarity(mean_stats.iloc[:, 1:])
    cos_df = pd.DataFrame(cosine, index=mean_stats.iloc[:, 1:].index)
    cos_df = pd.concat([mean_stats.player_name, cos_df], axis=1)
    all_players = cos_df.player_name.to_list()
    cos_df.columns = ['player_name'] + all_players
    return cos_df


def euclid_similarity_df():
    from scipy.spatial.distance import cdist
    euclid = cdist(mean_stats.iloc[:, 1:], mean_stats.iloc[:, 1:], 'euclid')
    euc_df = pd.DataFrame(euclid, index=mean_stats.iloc[:, 1:].index)
    euc_df = pd.concat([mean_stats.player_name, euc_df], axis=1)
    all_players = euc_df.player_name.to_list()
    euc_df.columns = ['player_name'] + all_players
    return euc_df


def manhattan_similarity_df():
    from scipy.spatial.distance import cdist
    manhattan = cdist(mean_stats.iloc[:, 1:], mean_stats.iloc[:, 1:], 'cityblock')
    man_df = pd.DataFrame(manhattan, index=mean_stats.iloc[:, 1:].index)
    man_df = pd.concat([mean_stats.player_name, man_df], axis=1)
    all_players = man_df.player_name.to_list()
    man_df.columns = ['player_name'] + all_players
    return man_df


def minkowski_similarity_df():
    from scipy.spatial.distance import cdist
    minkowski = cdist(mean_stats.iloc[:, 1:], mean_stats.iloc[:, 1:], 'minkowski')
    mink_df = pd.DataFrame(minkowski, index=mean_stats.iloc[:, 1:].index)
    mink_df = pd.concat([mean_stats.player_name, mink_df], axis=1)
    all_players = mink_df.player_name.to_list()
    mink_df.columns = ['player_name'] + all_players
    return mink_df


cosine_df = cosine_similarity_df()
euclid_df = euclid_similarity_df()
manhattan_df = manhattan_similarity_df()
minkowski_df = minkowski_similarity_df()


def similarity(sp, cos, euc, man, mink):
    import collections
    from operator import itemgetter
    similar_df = cos.loc[cos['player_name'] == sp]
    similar_df.set_index('player_name', inplace=True)
    cos_top_10 = similar_df.sort_values(by=sp, axis=1, ascending=False).iloc[:, 1:10]
    similar_df = euc.loc[euc['player_name'] == sp]
    similar_df.set_index('player_name', inplace=True)
    euc_top_10 = similar_df.sort_values(by=sp, axis=1, ascending=True).iloc[:, 1:10]
    similar_df = man.loc[man['player_name'] == sp]
    similar_df.set_index('player_name', inplace=True)
    man_top_10 = similar_df.sort_values(by=sp, axis=1, ascending=True).iloc[:, 1:10]
    similar_df = mink.loc[mink['player_name'] == sp]
    similar_df.set_index('player_name', inplace=True)
    mink_top_10 = similar_df.sort_values(by=sp, axis=1, ascending=True).iloc[:, 1:10]
    a_list = cos_top_10.columns.to_list()
    b_list = euc_top_10.columns.to_list()
    c_list = man_top_10.columns.to_list()
    d_list = mink_top_10.columns.to_list()
    comp_list = a_list + b_list + c_list + d_list
    occurrences = collections.Counter(comp_list)
    res = dict(sorted(occurrences.items(), key=itemgetter(1), reverse=True)[:10])
    return res


# a = 10
#
#
# def add(x, y, a):
#     z = (x + y) * a
#     return z
#
#
class SimilarPlayer(BaseModel):
    player: str
# #
# # #dict_of_players = similarity((SimilarPlayer.similar_player, cosine_df, euclid_df, manhattan_df, minkowski_df))
# #

@app.post('/similarplayer')
async def similar_player(sp: SimilarPlayer):
    dict_of_players = similarity((sp.player, cosine_df, euclid_df, manhattan_df, minkowski_df))
    return {'similar_players': dict_of_players}
# #
# #
# @app.get('/')
# def index():
#     return {'data': {'name': 'Lionel Messi'}}
#
#
# @app.get('/about')
# def about():
#     return {'data': 'about page'}

