import os , csv

with open("100MostStreamedSongs.csv", encoding='utf-8', errors='replace') as file:
    reader = csv.DictReader(file)
    total = 0
    for row in reader:
     dir = os.listdir()
     artist = row["Artist(s)"]
     print(artist)
    if artist not in dir:
        os.mkdir(artist)
    song = row["Song"]
    print(row["Song"])
    path = os.path.join(f"{artist}/", song)
    file = open(path, 'w')
    file.close()
          