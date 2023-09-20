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