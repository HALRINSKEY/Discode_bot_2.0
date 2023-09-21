import discord
from tracemalloc import start
import time
from discord import app_commands
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
MY_GUILD = discord.Object(id=)#サーバーID

class MyClient(discord.Client):
    leave_name = 0
    leave_time = 0

    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

#noticebot------------------------------------------------------------------------------
    async def on_voice_state_update(self, member, before, after):
        
        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        announceChannelIds = []
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = client.get_channel()

        if before.channel != after.channel:

            # 入室通知
            if after.channel is not None and after.channel.id in announceChannelIds:
            
                #退室して5秒以内に入室した際は通知しない
                if self.leave_name == member.name:
                    t = time.time() - self.leave_time

                    if t < 5:
                        pass                       
                    else:
                        await botRoom.send(member.name + " entered in " + after.channel.name)
       
                else:
                    await botRoom.send(member.name + " entered in " + after.channel.name)

            #退室処理
            if before.channel is not None and before.channel.id in announceChannelIds:
            
                self.leave_name = member.name
                self.leave_time = time.time()
#-----------------------------------------------------------------------------------------

client = MyClient(intents=intents)

#command----------------------------------------------------------------------------------
@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

@client.tree.command()
async def getserverid(interaction: discord.Interaction):
   """serverID"""
   serverId = interaction.guild.id
   await interaction.response.send_message(serverId)

@client.tree.command()
async def channel(interaction: discord.Interaction):
    """chanelID"""
    channels = {}
    for ch in client.get_all_channels():
        channels[ch.name] = str(ch.id)

    #ターミナルに表示したいとき
    #for name, id in channels.items():
    #    print("name:" + name + "    id:" + id)

    ch_id ="\n".join(["name:{0}      id:{1}".format(key, value) for (key, value) in channels.items()])
    await interaction.response.send_message(ch_id)

#------------------------------------------------------------------------------------------

client.run("token")
