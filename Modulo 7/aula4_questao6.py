import csv

def analisar_spotify():
    with open("spotify-2023.csv", "r", encoding="latin-1") as csvfile:
        reader = csv.DictReader(csvfile)
        top_musicas_por_ano = {}
        
        for row in reader:
            try:
                ano = int(row['released_year'])
                if 2012 <= ano <= 2022:
                    streams = int(row['streams'])
                    if ano not in top_musicas_por_ano or streams > top_musicas_por_ano[ano]['streams']:
                        top_musicas_por_ano[ano] = {
                            'track_name': row['track_name'],
                            'artist(s)_name': row['artist(s)_name'],
                            'streams': streams
                        }
            except ValueError:
                continue
        
        top_musicas = [
            [data['track_name'], data['artist(s)_name'], ano, data['streams']]
            for ano, data in sorted(top_musicas_por_ano.items())
        ]
        
        for musica in top_musicas:
            print(musica)

analisar_spotify()
