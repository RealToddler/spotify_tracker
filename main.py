# -*- coding: utf-8 -*-

import json
import os

class Spotify_Tracker:
    def __init__(self):
        self.data = []
        self.dates = ["2021-12", "2022-01", "2022-02", "2022-03", "2022-04", "2022-05", "2022-06", "2022-07", "2022-08", "2022-09", "2022-10", "2022-11"]
        for history in next(os.walk("data"), (None, None, []))[2]:
            with open(f"data/{history}", 'r', encoding="UTF-8") as f:
                self.data.append(json.load(f))

    
    def listening_time(self):
        total_ms = sum(
                [int(item[i]["msPlayed"]) for item in self.data for i in range(len(item)) \
                    for date in self.dates if date in item[i]["endTime"].split(" ")[0]]
                )
        seconds = int(total_ms/1000)%60
        minutes = int(total_ms/(1000*60))%60
        hours = int(total_ms/(1000*60*60))%24
        days = int(total_ms/(1000*60*60*24))
        return "%dd %dh %dmin %dsec." % (days, hours, minutes, seconds)

    
    def listening_time_per_artist(self):
        dico = {}
        for item in self.data:
            for i in range(len(item)):
                for date in self.dates:
                    if date in item[i]["endTime"].split(" ")[0]:
                        if item[i]["artistName"] in dico.keys():
                            dico[item[i]["artistName"]] += int(item[i]["msPlayed"])
                        else:
                            dico[item[i]["artistName"]] = int(item[i]["msPlayed"])

        dico = dict(sorted(dico.items(),  key=lambda kv: kv[1], reverse=True))
            
        for artist in dico:
            ms_played = dico[artist]
            seconds = int(ms_played/1000)%60
            minutes = int(ms_played/(1000*60))%60
            hours = int(ms_played/(1000*60*60))%24
            days = int(ms_played/(1000*60*60*24))
            dico[artist] = "%dd %dh %dmin %dsec." % (days, hours, minutes, seconds)
        
        return dico
    

    def listening_time_per_song(self):
        dico = {}
        for item in self.data:
            for i in range(len(item)):
                for date in self.dates:
                    if date in item[i]["endTime"].split(" ")[0]:
                        if item[i]["trackName"] in dico.keys():
                            dico[item[i]["trackName"]] += int(item[i]["msPlayed"])
                        else:
                            dico[item[i]["trackName"]] = int(item[i]["msPlayed"])

        dico = dict(sorted(dico.items(),  key=lambda kv: kv[1], reverse=True))
            
        for artist in dico:
            ms_played = dico[artist]
            seconds = int(ms_played/1000)%60
            minutes = int(ms_played/(1000*60))%60
            hours = int(ms_played/(1000*60*60))%24
            days = int(ms_played/(1000*60*60*24))
            dico[artist] = "%dd %dh %dmin %dsec." % (days, hours, minutes, seconds)
        
        return dico

        
tracker = Spotify_Tracker()
listening_time = tracker.listening_time()
print(listening_time, end="\n")


listening_time_per_artist = tracker.listening_time_per_artist()
for i in range(10):
    key = list(listening_time_per_artist.keys())[i]
    val = listening_time_per_artist[key]
    print(f"{key} : {val}")

listening_time_per_song = tracker.listening_time_per_song()
for i in range(10):
    key = list(listening_time_per_song.keys())[i]
    val = listening_time_per_song[key]
    print(f"{key} : {val}")