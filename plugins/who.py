from api import eve_xml, zkb


def handle(message, client):
    args = message.content[5:]

    char_id = eve_xml.get_entity_id_for_name(args)
    zkb_stats = zkb.query_character_stats(char_id)

    msg = "\n{} [{} - {}] \n{} \n{}".format(
            zkb_stats['info']['name'],
            zkb_stats['shipsDestroyed'],
            zkb_stats['shipsLost'],
            eve_xml.get_entity_name(zkb_stats['info']['corporationID']),
            eve_xml.get_entity_name(zkb_stats['info']['allianceID']))

    client.send_message(message.channel, msg)
