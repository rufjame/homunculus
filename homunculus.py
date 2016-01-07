import discord
import sys
from plugins import price, who
from util.discord_util import reply, log_in_client

# Configure what to load here. Keys represent commands, and
# each value represents the module that handles the associated
# command
loaded_modules = {'!price': price,
                  '!who': who}

client = discord.Client()
log_in_client(client)


@client.event
def on_message(message):
    if message.author == client.user:
        return
        
    #
    # Module commands
    #
    
    handled_by_module = False
    for m in loaded_modules:
        if message.content.startswith(m):
            loaded_modules[m].handle(message, client)
            handled_by_module = True
    
    
    #
    # Global commands
    #

    if handled_by_module:
        return
    
    # elif message.content.startswith('!help'):
    #     for m in modules:
    #         modules[m].help()

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
        loaded_modules[m].init()
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)


client.run()
