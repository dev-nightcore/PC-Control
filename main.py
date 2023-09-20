from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
import logging

import misc.screenshot as screenshot
import misc.hotkeys as hotkeys
import misc.media as media
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
start_message.sendmsg()

# -- Keyboards handler
@dp.message_handler(text=['/start'])
async def cmdStart(message: types.Message):
    if admin_id == message.chat.id:
        await message.answer(text="Main menu", reply_markup=keyboard.main_keyboard)
        await functions.deleteMessage(message)
    else: await message.answer(text="You`re not whitelisted!")

@dp.message_handler(text=['Hotkeys'])
async def cmdStart(message: types.Message):
    await message.answer(text="Hotkeys menu", reply_markup=keyboard.hotkey_keyboard)
    await functions.deleteMessage(message)

@dp.message_handler(text=['Controls'])
async def cmdStart(message: types.Message):
    await message.answer(text="Controls menu", reply_markup=keyboard.control_keyboard)
    await functions.deleteMessage(message)

@dp.message_handler(text=['Media']) 
async def cmdStart(message: types.Message):
    await message.answer(text="Media control menu", reply_markup=keyboard.media_keyboard)
    await functions.deleteMessage(message)

@dp.message_handler(text=['Screen']) 
async def cmdStart(message: types.Message):
    await message.answer(text="Screen menu", reply_markup=keyboard.screen_keyboard)
    await functions.deleteMessage(message)

@dp.message_handler(text=['🔙 Back'])
async def cmdStart(message: types.Message):
    await message.answer(text="Main menu", reply_markup=keyboard.main_keyboard)
    await functions.deleteMessage(message)
    message.reply_markup


# -- Media handlers, volume
@dp.message_handler(text="🔊")
async def volup(message: types.Message):
    if admin_id == message.chat.id:
        await media.volUp()
        await functions.deleteMessage(message)
    else: await message.answer(text="You`re not whitelisted!")
@dp.message_handler(text="🔇")
async def volmute(message: types.Message):
    if admin_id == message.chat.id:
        await media.volOff()
        await functions.deleteMessage(message)
    else: await message.answer(text="You`re not whitelisted!")
@dp.message_handler(text="🔉")
async def voldown(message: types.Message):
    if admin_id == message.chat.id:
        await media.volDown()
        await functions.deleteMessage(message)
    else: await message.answer(text="You`re not whitelisted!")


# -- Media handlers, tracks control
@dp.message_handler(text="⏪")
async def trackprev(message: types.Message):
    if admin_id == message.chat.id:
        await media.trackPrev()
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")
@dp.message_handler(text="⏯")
async def pause(message: types.Message):
    if admin_id == message.chat.id:
        await media.playPause()
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")
@dp.message_handler(text="⏩")
async def tracknext(message: types.Message):
    if admin_id == message.chat.id:
        await media.trackNext()
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")

# -- Media handlers, arrows controls
@dp.message_handler(text="⬆️")
async def arrowup(message: types.Message):
    if admin_id == message.chat.id:
        await media.arrowUp()
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")
@dp.message_handler(text="⬇️")
async def arrowDown(message: types.Message):
    if admin_id == message.chat.id:
        await media.arrowDown()
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")
@dp.message_handler(text="⬅️")
async def arrowleft(message: types.Message):
    if admin_id == message.chat.id:
        await media.arrowLeft()
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")
@dp.message_handler(text="➡️")
async def arrowright(message: types.Message):
    if admin_id == message.chat.id:
        await media.arrowRight()
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")

# -- Media open youtube
@dp.message_handler(text="play_yt")
async def play_yt(message: types.Message):
    await functions.deleteMessage(message)
    await media.play_youtube_video(message.get_args())
    await message.answer(
        f"<i>Video going to open.\nLink: <code>{message.get_args()}</code></i>",
        parse_mode="html",
    )

# -- Hotkeys handlers
@dp.message_handler(text="ALT+TAB")
async def altTab(message: types.Message):
    if admin_id == message.chat.id:
        await hotkeys.altTab()
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")

@dp.message_handler(text="ALT+F4")
async def altF4(message: types.Message):
    if admin_id == message.chat.id:
        await hotkeys.altF4()
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")

# -- Controls handlers
@dp.message_handler(text="Shutdown")
async def taimerStop(message: types.Message):
    if admin_id == message.chat.id:
        await control.shutdown()
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")

@dp.message_handler(text="Log out from user")
async def winL(message: types.Message):
    if admin_id == message.chat.id:
        await control.logOut()
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")

@dp.message_handler(text="Reboot")
async def reboot(message: types.Message):
    if admin_id == message.chat.id:
        await control.reboot()
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")

# -- Screen menu
@dp.message_handler(text="Screenshot")
async def altTab(message: types.Message):
    if admin_id == message.chat.id:
        await screenshot.screenshot(message)
        await functions.deleteMessage(message)
        await functions.answerSucsessAndDelete(message)
    else: await message.answer(text="You`re not whitelisted!")

# -- None handler
@dp.message_handler(text=" ")
async def none(message: types.Message):
    await functions.deleteMessage(message)

# -- executor
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)