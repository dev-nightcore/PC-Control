from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
import logging

import misc.screenshot as screenshot
import misc.hotkeys as hotkeys
import misc.volume as volume
import misc.control as control
import misc.functions as functions
import misc.keyboard as keyboard
import misc.start_message as start_message
import config as config


# -- Config
bot = Bot(config.bot_token)
admin_id = config.whitelisted_id

# -- Bot init
dp = Dispatcher(bot)
logging.basicConfig(
        format='| %(asctime)s | %(name)s | %(levelname)s |   %(message)s', datefmt='%m/%d/%Y %I:%M',
        level=logging.INFO)

start_message.sendMessage()

# -- Keyboards handler
@dp.message_handler(text_contains=['/start'])
async def cmdStart(message: types.Message):
    if admin_id == message.chat.id:
        await message.answer(text="Main menu", reply_markup=keyboard.main_keyboard)
        await functions.deleteMessage(message)
    else: await message.answer(text="You`re not whitelisted!")

@dp.message_handler(text_contains=['Hotkeys'])
async def cmdStart(message: types.Message):
    await message.answer(text="Hotkeys menu", reply_markup=keyboard.hotkey_keyboard)
    await functions.deleteMessage(message)

@dp.message_handler(text_contains=['Controls'])
async def cmdStart(message: types.Message):
    await message.answer(text="Controls menu", reply_markup=keyboard.control_keyboard)
    await functions.deleteMessage(message)

@dp.message_handler(text_contains=['Media']) 
async def cmdStart(message: types.Message):
    await message.answer(text="Media control menu", reply_markup=keyboard.media_keyboard)
    await functions.deleteMessage(message)

@dp.message_handler(text_contains=['Screen']) 
async def cmdStart(message: types.Message):
    await message.answer(text="Screen menu", reply_markup=keyboard.screen_keyboard)
    await functions.deleteMessage(message)

@dp.message_handler(text_contains=['🔙 Back'])
async def cmdStart(message: types.Message):
    await message.answer(text="Main menu", reply_markup=keyboard.main_keyboard)
    await functions.deleteMessage(message)
    message.reply_markup


# -- Media handlers, volume
@dp.message_handler(text_contains="🔊")
async def altF4(message: types.Message):
    if admin_id == message.chat.id:
        await volume.volUp()
        await functions.deleteMessage(message)
    else: await message.answer(text="You`re not whitelisted!")
@dp.message_handler(text_contains="🔇")
async def altF4(message: types.Message):
    if admin_id == message.chat.id:
        await volume.volOff()
        await functions.deleteMessage(message)
    else: await message.answer(text="You`re not whitelisted!")
@dp.message_handler(text_contains="🔉")
async def altF4(message: types.Message):
    if admin_id == message.chat.id:
        await volume.volDown()
        await functions.deleteMessage(message)
    else: await message.answer(text="You`re not whitelisted!")

# -- Media handlers, tracks control
@dp.message_handler(text_contains="⏪")
async def altF4(message: types.Message):
    if admin_id == message.chat.id:
        await volume.trackPrev()
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")
@dp.message_handler(text_contains="⏯")
async def altF4(message: types.Message):
    if admin_id == message.chat.id:
        await volume.playPause()
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")
@dp.message_handler(text_contains="⏩")
async def altF4(message: types.Message):
    if admin_id == message.chat.id:
        await volume.trackNext()
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")

# -- Hotkeys handlers
@dp.message_handler(text_contains="ALT+TAB")
async def altTab(message: types.Message):
    if admin_id == message.chat.id:
        await hotkeys.altTab()
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")

@dp.message_handler(text_contains="ALT+F4")
async def altF4(message: types.Message):
    if admin_id == message.chat.id:
        await hotkeys.altF4()
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")

# -- Controls handlers
@dp.message_handler(text_contains="Shutdown")
async def taimerStop(message: types.Message):
    if admin_id == message.chat.id:
        await control.shutdown()
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")

@dp.message_handler(text_contains="Log out from user")
async def winL(message: types.Message):
    if admin_id == message.chat.id:
        await control.logOut()
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")

@dp.message_handler(text_contains="Reboot")
async def reboot(message: types.Message):
    if admin_id == message.chat.id:
        await control.reboot()
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")

# -- Screen menu
@dp.message_handler(text_contains="Screenshot")
async def altTab(message: types.Message):
    if admin_id == message.chat.id:
        await screenshot.screenshot(message)
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")

@dp.message_handler(text_contains="Live Screenshot")
async def altTab(message: types.Message):
    if admin_id == message.chat.id:
        await screenshot.live_screenshot(message)
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")

# -- executor
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)