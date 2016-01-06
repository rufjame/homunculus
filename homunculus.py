import discord
from price import get_price_for_string, load_typeids_file


def log_in_client(client: discord.Client):
    with open('account') as f:
        str = f.read()
    name, pw = str.split(' ')
    client.login(name, pw)


client = discord.Client()
log_in_client(client)


def handle_price(args: str, channel):
        try:
            price, type = get_price_for_string(args.lower())
            client.send_message(channel,
                                "Lowest sell price for {} in jita: {:,.2f}"
                                .format(type, price))
        except KeyError:
            client.send_message(channel,
                                "Thing not found. Enter a thing I can find.")
        except Exception as err:
            print("Shit crashed and burned, error:", err)
            client.send_message(channel,
                                "Shit crashed and burned. Poke Az.")


@client.event
def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!price'):
        handle_price(message.content[7:], message.channel)

    if message.content.startswith('Are you there?'):
        client.send_message(message.channel,
                            "Yes, yes I am. No worries. Everything is fine.")

    if message.content.startswith('!ping'):
        client.send_message(message.channel,
                            "We're not doing this again.")

    if message.content.startswith('!trivia'):
        client.send_message(message.channel,
                            "Fuck you {}. Blame Fenrir."
                            .format(message.author.mention()))


@client.event
def on_ready():
    load_typeids_file()
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)

client.run()
