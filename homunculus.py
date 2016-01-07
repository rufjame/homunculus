import discord

from plugins import price, who

modules = [price,
           who]


def log_in_client(c: discord.Client):
    with open('account') as f:
        string = f.read()
    name, pw = string.split(' ')
    c.login(name, pw)


client = discord.Client()
log_in_client(client)


@client.event
def on_message(message):
    if message.author == client.user:
        return

    # if message.content.startswith('!help'):
    #     for m in modules:
    #         m.help()

    if message.content.startswith('!price'):
        price.handle(message, client)
        return

    if message.content.startswith('!who'):
        who.handle(message, client)
        return

    if message.content.startswith('Are you there?'):
        client.send_message(message.channel,
                            "Yes, yes I am. No worries. Everything is fine.")
        return

    # This needed to be done.
    if message.content.startswith('!poop'):
        client.send_message(message.channel,
                            "{} and Poop are friends."
                            .format(message.author.mention()))
        return

    if message.content.startswith('!ping'):
        client.send_message(message.channel,
                            "We're not doing this again.")
        return

    if message.content.startswith('!trivia'):
        client.send_message(message.channel,
                            "Fuck you {}. Blame Fenrir."
                            .format(message.author.mention()))
        return


@client.event
def on_ready():
    for m in modules:
        m.init()
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)


client.run()
