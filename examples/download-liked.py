#!/bin/env python

import ytm
import ytmusicapi
import pprint as pp
import json
import os

ym=ytmusicapi.YTMusic('oauth.json')
liked=ym.get_liked_songs()

savedSongsFile="savedSongIDs.json"
oldIDs=[]
if os.access(savedSongsFile, os.R_OK):
    with open(savedSongsFile, "r") as songs:
        oldIDs = json.load(songs)

IDs=[]
for l in liked['tracks']:
    IDs.append(l['videoId'])

diffIDs=[]
for i in IDs:
    if i in oldIDs:
        continue
    diffIDs.append(i)

if len(diffIDs) == 0:
    print("no new liked songs")
    exit(0)

api=ytm.YouTubeMusicDL()
for i in diffIDs:
    print("download", i, end='', flush=True)
    try:
        res=api.download_song(song_id=i)
        print("{} - {} - {}".format(str(res['artist'] or ''), str(res['album'] or ''), str(res['title'] or '')))
    except Exception as e:
        with open(i, "w") as log:
            pp.pprint(e, stream=log)

# save the whole list
with open(savedSongsFile, "w") as songs:
    json.dump(IDs, songs)
