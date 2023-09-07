import ctypes
import pyautogui as gui

async def winL():
    ctypes.windll.user32.LockWorkStation()

async def altF4():
    gui.hotkey("alt", "f4")

async def altTab():
    gui.hotkey("alt", "tab")