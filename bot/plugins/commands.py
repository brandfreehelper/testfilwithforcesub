#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG & @Mrk_YT

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '๐Join Main Channel๐', url=f"https://t.me/song_requestgroup"
                                )
                        ],
                        [
                            InlineKeyboardButton
                                (
                                    '๐ Bot Updates ๐', url=f"https://t.me/song_requestgroup"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await update.bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '๐จโ๐ผ ๐ณ๐๐๐๐๐๐๐๐๐ ๐จโ๐ผ', url="https://t.me/Mo_TECH_YT"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await update.bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '๐จโ๐ผ ๐ณ๐๐๐๐๐๐๐๐๐ ๐จโ๐ผ', url="https://t.me/Mo_TECH_YT"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('๐จโ๐ผCreater', url=f'https://t.me/{MRK_YT_MASTER}'),
        InlineKeyboardButton('Help ๐ค', callback_data="help")
    ],[
        InlineKeyboardButton('๐ฃ๏ธGroup', url=f'{MT_GROUP}'),
        InlineKeyboardButton('Channel๐', url=f'{MT_CHANNEL}')
    ],[
        InlineKeyboardButton('๐ฅ๏ธ Tutorial Video ๐ฅ๏ธ', url='https://youtu.be/OTqZmADyOjU')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('๐? ๐ท๐๐๐', callback_data='start'),
        InlineKeyboardButton('๐ฐ๐๐๐๐ ๐ฉ', callback_data='about')
    ],[
        InlineKeyboardButton('๐ ๐ฒ๐๐๐๐ ๐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('๐ค Mrk YT๐ค', url='https://t.me/MRK_YT'),
        InlineKeyboardButton('Skp KP๐ค', url='https://t.me/Skp_Kp')
    ],[
        InlineKeyboardButton('๐ค AlbertEinstein ๐ค', url='https://t.me/AlbertEinsteinTG')
    ],[
        InlineKeyboardButton('๐? Home', callback_data='start'),
        InlineKeyboardButton('Close ๐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
