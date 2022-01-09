import os
import telebot
import fnmatch

bot = telebot.TeleBot("your token goes here", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, """\
This bot can download songs / albums / playlists from Spotify as FLAC and MP3.
Send a spotify song link to see the magic.
Use /flac for FLACs and use /mp3 for MP3s.
For example: /flac https://open.spotify.com/album/5LFzwirfFwBKXJQGfwmiMY

This bot uses spotDL (https://github.com/spotDL). Hats off to their work.
This bot uses pyTelegramBotAPI (https://github.com/eternnoir/pyTelegramBotAPI).
Bot source code is available at https://github.com/rain2wood/spotBot-OSS.
\
""")

@bot.message_handler(commands=['flac'])
def download_flac(message):
    chat_id = message.chat.id
    songLink = message.text
    str = songLink
    if str.find("track")!=-1:
        print("is track")
        realSong = songLink.replace("/flac", "")
        bot.reply_to(message, "Fetching song...")
        DownloadSong = "bash magic.sh '{}' -f -t".format(realSong)
        os.system(DownloadSong)
        f = open("link.txt", "r")
        text = f.read()
        bot.send_message(chat_id, text)
        cleansong = "rm -rf link.txt"
        os.system(cleansong)
    elif str.find("album")!=-1 or str.find("playlist")!=-1:
        print("is album or playlist")
        realSong = songLink.replace("/flac", "")
        bot.reply_to(message, "Fetching album / playlist. This will take a while.")
        DownloadSong = "bash magic.sh '{}' -f -a".format(realSong)
        os.system(DownloadSong)
        f = open("link.txt", "r")
        text = f.read()
        bot.send_message(chat_id, text)
        cleansong = "rm -rf link.txt"
        os.system(cleansong)
    else:
        bot.send_message(chat_id, "bot does not support non-track")

@bot.message_handler(commands=['mp3'])
def download_mp3(message):
    chat_id = message.chat.id
    songLink = message.text
    str = songLink
    if str.find("track")!=-1:
        print("is track")
        realSong = songLink.replace("/mp3", "")
        bot.reply_to(message, "Fetching song...")
        DownloadSong = "bash magic.sh '{}' -m -t".format(realSong)
        os.system(DownloadSong)
        f = open("link.txt", "r")
        text = f.read()
        bot.send_message(chat_id, text)
        cleansong = "rm -rf link.txt"
        os.system(cleansong)
    elif str.find("album")!=-1 or str.find("playlist")!=-1:
        print("is album or playlist")
        realSong = songLink.replace("/mp3", "")
        bot.reply_to(message, "Fetching album / playlist. This will take a while.")
        DownloadSong = "bash magic.sh '{}' -m -a".format(realSong)
        os.system(DownloadSong)
        f = open("link.txt", "r")
        text = f.read()
        bot.send_message(chat_id, text)
        cleansong = "rm -rf link.txt"
        os.system(cleansong)
    else:
        bot.send_message(chat_id, "bot does not support non-track")

bot.infinity_polling()

