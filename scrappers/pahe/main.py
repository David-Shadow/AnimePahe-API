from AnilistPython import Anilist
anilist = Anilist()
import logging 
logger = logging.getLogger("AnimePahe")
from curl_cffi.requests import get

class AnimePahe():
    def __init__(self):
        self.host = "https://animepahe.ru/"

    def search(self, query):
        try:
            url = f"{self.host}api?m=search&q={query}"
            r = get(url, impersonate="chrome101")
            dt = r.json()['data']

            data = dt.copy()
            for dictionary in data:
                dictionary["anilistId"] = dictionary.pop("id")
                dictionary["id"] = dictionary.pop("session")
            results = {"results": data}
            return results
            
        except Exception as e:
            logger.info(f"AnimePahe - {e}")
            results = {"results": [e]}
            return results

    def info(self, id):
        try:
            url = f"{self.host}api?m=release&id={id}&sort=episode_asc"
            r = get(url, impersonate="chrome101")
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
            logger.info(f"AnimePahe - {e}")
            episodes = {"episodes": [e]}
            return episodes




