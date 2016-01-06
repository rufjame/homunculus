import requests
from xml.etree import ElementTree


def get_entity_id_for_name(name: str) -> int:
    url = "https://api.eveonline.com/eve/OwnerID.xml.aspx?names=" + name
    result = requests.get(url)
    tree = ElementTree.fromstring(result.content)

    # first: Current Time, Rowset, or Cached Until
    # second: row in rowset (0)
    # third: accessing the actual attribute in the result row.
    return tree[1][0][0].attrib['ownerID']


def get_entity_name(id: int) -> str:
    url = "https://api.eveonline.com/eve/CharacterName.xml.aspx?ids=" + str(id)
    result = requests.get(url)
    tree = ElementTree.fromstring(result.content)

    # first: Choice between Current Time (0), Rowset (1, this), Cached Until(2)
    # second: row in a rowset (0)
    # third: accessing the name for the name, id tuple.
    return tree[1][0][0].attrib['name']
