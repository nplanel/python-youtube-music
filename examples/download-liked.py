#!/bin/env python

import ytm
import ytmusicapi
import pprint as pp

ym=ytmusicapi.YTMusic('oauth.json')
liked=ym.get_liked_songs()

IDs=[]
for l in liked['tracks']:
    IDs.append(l['videoId'])

api=ytm.YouTubeMusicDL()
for i in IDs:
    print("download", i)
    try:
        res=api.download_song(song_id=i)
    except Exception as e:
        with open(i, "w") as log:
            pp.pprint(e, stream=log)

