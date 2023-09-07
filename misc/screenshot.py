import pyautogui as gui

gui.FAILSAFE = False


async def screenshot(message):
    gui.screenshot('screenShot.png')
    await message.answer_photo(open('screenShot.png', 'rb'))

async def live_screenshot(message):
    gui.screenshot('live_screen.png')
    await message.answer_photo(open('live_screen.png', 'rb'))