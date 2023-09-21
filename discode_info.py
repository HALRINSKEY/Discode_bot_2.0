import discord


intents = discord.Intents.default()
intents.message_content = True


class MyClient(discord.Client):

    async def on_ready(self):
      
        print(client.guilds)

        channels = {}
        for ch in client.get_all_channels():
            channels[ch.name] = str(ch.id)

        for name, id in channels.items():
            print("name:" + name + "    id:" + id)

client = MyClient(intents=intents)

token = input("Input bot's token\n")
client.run(token)