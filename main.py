"""
Main bot file
"""

from aiogram import Bot, Dispatcher, types, executor
from config import *
from messages import *
import os
import glob
import re
import logging
from datetime import datetime

# Rename old log file
list_of_files = sorted( filter( os.path.isfile,
                        glob.glob(f"{logs_folder}/" + '*') ) )
greates_num = 0
for file_path in list_of_files:
    if int(re.findall(r'\d+', file_path)[0]) > greates_num: greates_num = int(re.findall(r'\d+', file_path)[0])
if os.path.isfile(f"{logs_folder}/bot0.log"): os.rename(f"{logs_folder}/bot0.log", f"{logs_folder}/bot{greates_num+1}.log")

logging.basicConfig(filename=f"{logs_folder}/bot0.log", level=logging.DEBUG) # Create new log

def out(data, message=None): # Function for printing line to console&log
    out_data = "[" + str(datetime.now()) + "] | "
    if message: out_data += f"{message.from_user.id}/{message.from_user.username} | "
    else: out_data += "App | "
    out_data += data
    print(out_data)
    logging.info(out_data)

# Initing bot
out("Starting bot...")
_bot = Bot(token=bot["token"])
dp = Dispatcher(_bot)
out("Bot started!")

@dp.message_handler(commands=['start']) # Start command handler
async def start_message(message: types.Message):
    out("Got start msg", message)
    await _bot.send_message(message.from_user.id, start_msg, parse_mode="html")

@dp.message_handler(commands=['checkid']) # Check telegram id command handler
async def check_id_message(message: types.Message):
    out("Checked his/her id", message)
    await _bot.send_message(message.from_user.id, message.from_user.id, parse_mode="html")

@dp.message_handler(commands=['checkadmin']) # Check if you are admin command handler
async def check_admin_message(message: types.Message):
    admin = False
    for key in admin_users:
        if message.from_user.id == admin_users[key]:
            admin = True
            break
    out("Checked if he/she is admin", message)
    if admin: await _bot.send_message(message.from_user.id, admin_msg, parse_mode="html")
    else: await _bot.send_message(message.from_user.id, not_admin_msg, parse_mode="html")

@dp.message_handler(content_types=['text']) # Check size and forward user's text message to admin
async def send_to_admin(message: types.Message):
    out("Got text only", message)
    msg_len = len(message.text)
    if msg_len >= max_symbols:
        out(f"Too long msg {msg_len}", message)
        await _bot.send_message(message.from_user.id, too_long_news_msg + str(msg_len - max_symbols) + "</b> symbols!", parse_mode="html")
    elif msg_len <= min_symbols:
        out(f"Too short msg {msg_len}", message)
        await _bot.send_message(message.from_user.id, too_short_news_msg + str(min_symbols - msg_len) + "</b> symbols!", parse_mode="html")
    else:
        print("[" + str(datetime.now()) + f"] | {message.from_user.id}/{message.from_user.username} | Text ok")
        await _bot.send_message(message.from_user.id, news_sent_msg, parse_mode="html")
        for key in admin_users:
            answer = str(message.text) + "\n\n<b>From id:</b> " + str(message.from_user.id) + "\n<b>From username:</b> " + str(message.from_user.username)
            await _bot.send_message(admin_users[key], answer, parse_mode="html")
            await _bot.send_message(admin_users[key], devider, parse_mode="html")
        out("Message forwarded to admins", message)

@dp.message_handler(content_types=['photo', 'video', 'audio', 'document', 'voice']) # Check size and forward user's message with attachments to admin
async def send_to_admin(message):
    out("Got msg with attachments", message)
    try: # If attachment with caption
        msg_len = len(message.caption)
        if msg_len >= max_symbols:
            out(f"Too long msg {msg_len}", message)
            await _bot.send_message(message.from_user.id, too_long_news_msg + str(msg_len - max_symbols) + "</b> symbols!", parse_mode="html")
        elif msg_len <= min_symbols:
            out(f"Too short msg {msg_len}", message)
            await _bot.send_message(message.from_user.id, too_short_news_msg + str(min_symbols - msg_len) + "</b> symbols!", parse_mode="html")
        else:
            out("Text ok", message)
            await _bot.send_message(message.from_user.id, news_sent_msg, parse_mode="html")
            for key in admin_users:
                answer = str(message.caption) + "\n\n<b>From id:</b> " + str(message.from_user.id) + "\n<b>From username:</b> " + str(message.from_user.username)
                await _bot.send_message(admin_users[key], answer, parse_mode="html")
                if message.photo: await _bot.send_photo(admin_users[key], message.photo.file_id)
                if message.video: await _bot.send_video(admin_users[key], message.video.file_id)
                if message.audio: await _bot.send_audio(admin_users[key], message.audio.file_id)
                if message.document: await _bot.send_document(admin_users[key], message.document.file_id)
                if message.voice: await _bot.send_voice(admin_users[key], message.voice.file_id)
                await _bot.send_message(admin_users[key], devider, parse_mode="html")
                out("Message forwarded to admins", message)
    except TypeError: # If attachment without caption
        for key in admin_users:
            if message.photo: await _bot.send_photo(admin_users[key], message.photo.file_id)
            if message.video: await _bot.send_video(admin_users[key], message.video.file_id)
            if message.audio: await _bot.send_audio(admin_users[key], message.audio.file_id)
            if message.document: await _bot.send_document(admin_users[key], message.document.file_id)
            if message.voice: await _bot.send_voice(admin_users[key], message.voice.file_id)
            await _bot.send_message(admin_users[key], devider, parse_mode="html")
        out("Message forwarded to admins, no text", message)
    
if __name__ == "__main__": # Start bot
    executor.start_polling(dp, skip_updates=True)
