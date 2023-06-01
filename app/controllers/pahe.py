from flask import Blueprint, jsonify
from scrappers.pahe.main import AnimePahe
from scrappers.pahe.download import pahe_download

pahe = Blueprint('pahe', __name__)
animepahe = AnimePahe()
import logging
logger = logging.getLogger("pahedl")
@pahe.route('/')
def pahe_home():
    result = {"Intro":"Welcome to the animepahe provider: check out the provider's website @ https://animepahe.ru/","routes":["/:query","/info/:anime-session","/watch/:anime-session/:episode-session"],"documentation":"Not Even Exist. lol", "Note:":"It takes 10-15s to scrap and provide links"}
    
    return jsonify(result)
    
@pahe.route('/<query>')
def pahe_query(query):
    return animepahe.search(query)

@pahe.route('/info/<id>')
def pahe_info(id):
    return animepahe.info(id)


@pahe.route('/watch/<episodeId>')
def pahe_episode(episodeId):
    try:
        return jsonify(pahe_download(episodeId))
    except Exception as e:
        logger.info(f"AnimePahe - {e}")
        return jsonify({"sources": []})


