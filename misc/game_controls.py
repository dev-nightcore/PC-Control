import subprocess
from config import bot
from aiogram import types
import time
import pyautogui as gui
import keyboard

async def openRust():
    subprocess.call(['C:\Program Files (x86)\Steam\steamapps\common\Rust\\Rust.exe'])

async def connect_to_server(message: types.Message, args):
    if len(args) < 5:
        message.answer("Please check the IP!")
    else:
        subprocess.call(['C:\Program Files (x86)\Steam\steamapps\common\Rust\\Rust.exe'])
        time.sleep(50)
        gui.hotkey("f1")
        time.sleep(0.5)
        keyboard.write(f"connect {args}")
        gui.hotkey("enter")
