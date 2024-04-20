# import requests, json, os
# from requests.auth import HTTPBasicAuth

# client_ID = os.environ['CLIENT_ID']
# client_Secret = os.environ['CLIENT_SECRET']

# url = "https://accounts.spotify.com/api/token"
# data = {"grant_type": "client_credentials"}
# auth = HTTPBasicAuth(client_ID, client_Secret)

# response = requests.post(url, data=data, auth=auth)
# accessToken = response.json()['access_token']

# url = 'https://api.spotify.com/v1/search'
# header = {"Authorization": f"Bearer {accessToken}"}
# search = 'remaster%20track:Doxy%20artist:Miles%20Davis'

# fullURL = f"{url}?q={search}&type=track&limit=5"

# reponse = requests.get(fullURL, headers=header)
# data = reponse.json()


# # print(response.ok)
# # print(response.json())
# # print(response.status_code)