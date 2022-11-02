import json

genre_list = ["국내드라마", "국내영화", "댄스", "랩/힙합", "록/메탈", "발라드", "성인가요/트로트", "일렉트로니카", "재즈", "포크/블루스", "R&B/Soul","인디음악"]


with open('song.json', 'r',encoding='UTF-8') as f:
    songs = json.load(f)


new_list = []
for song in songs:
    new_data = {'model': 'songs.song'}
    if song ["genre"]:      
        genres = song["genre"].split(', ')
        genre_int_list = []
        for genre in genres:
            genre_int = genre_list.index(genre) + 1
            genre_int_list.append(genre_int)
        song['genre'] = genre_int_list

    else:
        song["genre"] = []

    new_data["fields"] = song
    new_list.append(new_data)

with open('songs_data.json', 'w', encoding='UTF-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)


