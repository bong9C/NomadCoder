# 25.08.09, 영화사이트 읽어오기

import requests

movie_ids = [
    234, 680, 550, 185, 641, 515042,
    152532, 120467, 872585,906126, 84030
]

websites = "https://nomad-movies.nomadcoders.workers.dev/movies"

for movie in movie_ids:
    movie_url = f"{websites}/{movie}"
    response = requests.get(movie_url)
    print(" ")
    print(response.status_code)

    if response.status_code == 200:
        data = response.json()
        print("🎥title : ", data["title"])
        print("🍿overview : ", data["overview"])
        print("⭐vote_average : ", data["vote_average"])