import pandas as pd
import numpy as np
import Recommenders as Recommenders


# def data_preprocessing():
#     song_df_1 = pd.read_csv('10000.txt', delimiter="\t")
#     dict = {'b80344d063b5ccb3212f76538f3d9e43d87dca9e': 'user_id', 'SOAKIMP12A8C130995': 'song_id', '1': 'listen_count'}
#     song_df_1.rename(columns=dict,
#                      inplace=True)
#     song_df_1.head()
#
#     song_df_2 = pd.read_csv('song_data.csv')
#     song_df_2.head()
#
#     # combine both data
#     song_df = pd.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on='song_id', how='left')
#     song_df.head()
#
#     # creating new feature combining title and artist name
#     song_df['song'] = song_df['title'] + ' - ' + song_df['artist_name']
#
#     # taking top 10k samples for quick results
#     song_df = song_df.head(10000)
#
#     # cummulative sum of listen count of the songs
#     song_grouped = song_df.groupby(['song']).agg({'listen_count': 'count'}).reset_index()
#     song_grouped.head()
#
#     grouped_sum = song_grouped['listen_count'].sum()
#     song_grouped['percentage'] = (song_grouped['listen_count'] / grouped_sum) * 100
#     song_grouped.sort_values(['listen_count', 'song'], ascending=[0, 1])
#     song_df.to_csv('my-songs.csv', index=False)
#     return song_df


def popularity(user_id):
    song_df = pd.read_csv('song_data.csv')
    pr = Recommenders.popularity_recommender_py()
    pr.create(song_df, 'user_id', 'song')
    # print(pr.recommend(song_df['user_id'][5]))
    return pr.recommend(user_id)


def item_similarity(user_id):
    # item similarity
    song_df = pd.read_csv('my-songs.csv')
    ir = Recommenders.item_similarity_recommender_py()
    ir.create(song_df, 'user_id', 'song')
    # user_items = ir.get_user_items(song_df['user_id'][5])
    # display user songs history
    # for user_item in user_items:
    #     print(user_item)
    # give song recommendation for that user
    return ir.recommend(user_id)
    # give related songs based on the words
    # print( ir.get_similar_items(['Oliver James - Fleet Foxes', 'The End - Pearl Jam']))
