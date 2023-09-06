import pyautogui as gui

async def volUp():
    gui.hotkey("volumeup")


async def volOff():
    gui.hotkey("volumemute")


async def volDown():
    gui.hotkey("volumedown")


async def trackPrev():
    gui.hotkey("prevtrack")


async def playPause():
    gui.hotkey("playpause")


async def trackNext():
    gui.hotkey("nexttrack")
