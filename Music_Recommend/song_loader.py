import json

with open('song.json', 'r',encoding='UTF-8') as f:
    songs = json.load(f)

new_list = []
for song in songs:
    new_data = {'model': 'songs.song'}
    new_data["fields"] = song
    new_list.append(new_data)

with open('songs_data.json', 'w', encoding='UTF-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)


