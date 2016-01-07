import requests

ZKB_API_ROOT = 'https://zkillboard.com/api'


def stats_character_id_query(char_id: int) -> str:
    return "{}/stats/characterID/{}/".format(ZKB_API_ROOT, str(char_id))


def fetch_json_api(url: str) -> dict:
    return requests.get(url).json()


# High-level access.

def query_character_stats(char_id: int) -> dict:
    return fetch_json_api(stats_character_id_query(char_id))
