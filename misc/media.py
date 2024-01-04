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

async def arrowRight():
    gui.hotkey("right")
async def arrowLeft():
    gui.hotkey("left")
async def arrowUp():
    gui.hotkey("up")
async def arrowDown():
    gui.hotkey("down")