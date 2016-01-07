import discord
from plugins import price, who
from util.discord_util import reply

loaded_modules = [price,
                  who]


def log_in_client(c: discord.Client):
    with open('account') as f:
        line = f.read()
    name, pw = line.split(' ')
    c.login(name, pw)


client = discord.Client()
log_in_client(client)


@client.event
def on_message(message):
    if message.author == client.user:
        return

    # elif message.content.startswith('!help'):
    #     for m in modules:
    #         m.help()

    elif message.content.startswith('!price'):
        price.handle(message, client)

    elif message.content.startswith('!who'):
        who.handle(message, client)

    elif message.content.startswith('Are you there?'):
        reply(client, message, "Yes, yes I am. No worries. Everything is fine.")

    # This needed to be done.
    elif message.content.startswith('!poop'):
        post = "{} and Poop are friends."\
            .format(message.author.mention())
        reply(client, message, post)

    elif message.content.startswith('!ping'):
        reply(client, message, "We're not doing this again.")

    elif message.content.startswith('!trivia'):
        post = "Fuck you, {}. Blame Fenrir."\
            .format(message.author.mention())
        reply(client, message, post)


@client.event
def on_ready():
    for m in loaded_modules:
        m.init()
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)


client.run()
