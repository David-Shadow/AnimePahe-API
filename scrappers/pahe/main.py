import requests
from AnilistPython import Anilist
anilist = Anilist()

class AnimePahe():
    def __init__(self):
        self.host = "https://animepahe.ru/"

    def search(self, query):
        try:
            url = f"{self.host}api?m=search&q={query}"
            r = requests.get(url)
            dt = r.json()['data']

            data = dt.copy()
            for dictionary in data:
                dictionary["anilistId"] = dictionary.pop("id")
                dictionary["id"] = dictionary.pop("session")
            results = {"results": data}
            return results
            
        except:
            results = {"results": []}
            return results

    def info(self, id):
        try:
            url = f"{self.host}api?m=release&id={id}&sort=episode_asc"
            r = requests.get(url)
            result = r.json()['data']

            updated_result = []

            for data in result:
                updated_data = data.copy()
                for key, value in data.items():
                    if key == "session":
                        updated_data["episodeId"] = f"{id}${value}"
                        del updated_data[key]
                updated_result.append(updated_data)

            episodes = {"episodes": updated_result}
            return episodes

        except Exception as e:
            print(e)
            episodes = {"episodes": []}
            return episodes




