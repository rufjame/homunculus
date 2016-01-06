import requests

EVE_C_ROOT = 'https://api.eve-central.com/api/marketstat/json'
JITA_SYSTEM_ID = 30000142
TYPEIDS_CSV = 'typeid.csv'

type_dict = dict()
type_id_dict = dict()


def handle(message, client):
    args = message.content[7:]

    try:
        price, item_type = get_price_for_string(args.lower())
        client.send_message(message.channel,
                            "Lowest sell price for {} in jita: {:,.2f}"
                            .format(item_type, price))
    except KeyError:
        client.send_message(message.channel,
                            "Thing not found. Enter a thing I can find.")
    except Exception as err:
        print("Shit crashed and burned, error:", err)
        client.send_message(message.channel,
                            "Shit crashed and burned. Poke Az.")


def get_price_for_string(type_name: str):
    # Shortcut.
    if type_name == "plex":
        return get_jita_sell_price(29668), "PLEX"
    else:
        return get_jita_sell_price(
                look_up_type_id(type_name)), look_up_type_name(
                look_up_type_id(type_name))


def get_jita_sell_price(type_id: int):
    return get_jita_orders(type_id)[0]['sell']['min']


def get_jita_orders(type_id: int):
    url = construct_query_url(type_id)
    return request_url(url)


def request_url(url: str):
    return requests.get(url).json()


def construct_query_url(type_id: int, system_id: int = JITA_SYSTEM_ID) -> str:
    return "{}?typeid={}&usesystem={}".format(
            EVE_C_ROOT, type_id, system_id)


def look_up_type_name(type_id: int) -> str:
    print("Looking up ", type_id)
    return type_id_dict[type_id]


def look_up_type_id(type_name: str) -> id:
    print("Looking up ", type_name)
    try:
        return type_dict[type_name.strip()]
    except KeyError:
        for key in type_dict.keys():
            if key.startswith(type_name.strip()):
                return type_dict[key]
            if key.endswith(type_name.strip()):
                return type_dict[key]
        raise KeyError


def load_typeids_file(path: str):
    with open(path, 'r', encoding='utf8') as f:
        for line in f:
            type_id_raw = line[:7]
            type_name_raw = line[8:]

            type_name = type_name_raw.lower().strip()
            type_id = type_id_raw.strip()

            type_id_dict[type_id] = type_name
            type_dict[type_name] = type_id


def init():
    load_typeids_file(TYPEIDS_CSV)
