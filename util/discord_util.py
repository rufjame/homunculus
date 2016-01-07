import discord


def reply(client: discord.Client, message: discord.Message, post: str):
    client.send_message(message.channel, post)
