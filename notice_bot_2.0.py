import discord
from tracemalloc import start
import time

intents = discord.Intents.default()
intents.message_content = True

leave_name = 0
leave_time = 0


class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        self.botRoom = client.get_channel(966831929058025482) 

#noticebot------------------------------------------------------------------------------
    async def on_voice_state_update(self, member, before, after):    
        global leave_name
        global leave_time

        # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
        if before.channel != after.channel:

 
            # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
            announceChannelIds = [966831929058025483]
 

            # 入室通知
            if after.channel is not None and after.channel.id in announceChannelIds:
            
                #退室して5秒以内に入室した際は通知しない
                if leave_name == member.name:
                    t = time.time() - leave_time

                    if t < 5:
                        pass
                    else:
                        await self.botRoom.send(member.name + " entered in " + after.channel.name)
       
                else:
                    await self.botRoom.send(member.name + " entered in " + after.channel.name)

        #退室
        if before.channel is not None and before.channel.id in announceChannelIds:
            
            leave_name = member.name
            leave_time = time.time()
#-----------------------------------------------------------------------------------------

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith("/hello"):
            await message.channel.send("hello")

        if message.content.startswith("/channel"):  #channel id
            channels = {}
            for ch in client.get_all_channels():
                channels[ch.name] = str(ch.id)

            for name, id in channels.items():
                await self.botRoom.send("name:" + name + "    id:" + id)


client = MyClient(intents=intents)
client.run("token")
