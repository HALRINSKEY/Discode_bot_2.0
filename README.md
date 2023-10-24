# Discode_bot_2.0
動作環境

python 3.11 

discord.py 2.3.2 

windows 10 

## 通知ボット作動イメージ
![noticebot](https://github.com/HALRINSKEY/Discode_bot_2.0/assets/50315416/7d0e22b4-1978-44e7-b374-2aa5374bddc0)

## 使い方

### Botの作成

1.<https://discord.com/developers/applications>にアクセスし

Applicationタブの**New Application**で新規botを作成します

<img width="1128" alt="スクリーンショット 2023-10-20 113945" src="https://github.com/HALRINSKEY/Discode_bot_2.0/assets/50315416/90279cca-16a5-4f72-8938-7766e32ac981">

<br>2.Botタブに移動しPUBLIC BOT、PRESENCE INTENT、SERVER MEMBERS、INTENT MESSAGE、CONTENT INTENTをONにします

<img width="1128" alt="スクリーンショット 2023-10-20 133306" src="https://github.com/HALRINSKEY/Discode_bot_2.0/assets/50315416/9c335263-da54-4e07-b551-e9a0621aa631">

<br>3.OAuth2 > URL Generatorタブに移動し

**SCORES > Bot**と**BOT PERMISSIONS > Administrator**にチェックを入れます

<br>4.生成されたURLにアクセスしサーバーにBotを招待します(サーバーの管理者である必要があります)

<img width="1128" alt="スクリーンショット 2023-10-20 115641" src="https://github.com/HALRINSKEY/Discode_bot_2.0/assets/50315416/4a994f79-2b5d-4ad2-b0c9-50caae12df8e">

<br>5.Botタブのトークンを控えてください

<img width="1128" alt="スクリーンショット 2023-10-20 135415" src="https://github.com/HALRINSKEY/Discode_bot_2.0/assets/50315416/44306dd7-a6e0-4c31-ac95-776c06688346">



### Botの導入

1.pythonがインストールされている環境でdiscord_info.pyを起動し、ターミナル上で控えてあるトークンを入力します

2.Botが参加しているサーバーのID(Guild ID)と各チャンネルのIDが表示されます

![スクリーンショット 2023-10-24 190244](https://github.com/HALRINSKEY/Discode_bot_2.0/assets/50315416/b4074e28-ddc6-4c29-8a10-fd174ae8d7e0)

<br>3.notice_bot_2.0.pyをエディタで開き必要な情報を入力します。

![スクリーンショット 2023-10-24 190701](https://github.com/HALRINSKEY/Discode_bot_2.0/assets/50315416/550f4ae4-97c5-4367-8c04-8eae0303d53f)

<br>※トークンはダブルクォーテーションあるいはシングルクォーテーションで囲んで文字列で指定してください  "token"

※入退室を監視したいチャンネルが複数ある場合は , 区切りでで指定してください　EnterChannelID = [channel1_ID, channel2_ID] 

<br>notice_bot_2.0.pyを実行すると指定されたテキストチャンネルに通知がされます

<br>

### 参考サイト

https://discordpy.readthedocs.io/ja/latest/

https://tech-cci.io/archives/6412

https://qiita.com/sizumita/items/9d44ae7d1ce007391699

https://qiita.com/1ntegrale9/items/9d570ef8175cf178468f

https://qiita.com/mtb_beta/items/d257519b018b8cd0cc2e













