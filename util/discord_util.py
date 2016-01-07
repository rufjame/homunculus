import discord


def reply(client: discord.Client, message: discord.Message, post: str):
    client.send_message(message.channel, post)


def log_in_client(c: discord.Client):
    with open('account') as f:
        line = f.read()
    name, pw = line.strip().split(' ')
    c.login(name, pw)
