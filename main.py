import logging
from aiogram import types, Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
import os
import easygui

import misc.screenshot as screenshot
import misc.hotkeys as hotkeys
import misc.volume as volume
import misc.control as control

bot = Bot("5560433951:AAHUIe0mtmmz6h4ntbZ-pvCAYIIXRFvoIHY")
admin_id = ''

dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


@dp.on_startup()
async def cmdStart(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Hotkeys","Media","Control"]
    keyboard.add(*buttons)
    await message.answer("PC Control >> Запущен", reply_markup=keyboard)




@dp.message_handler(text_contains="ALT+TAB")
async def altTab(message: types.Message):
    hotkeys.altTab()


@dp.message_handler(text_contains="ALT+F4")
async def altF4(message: types.Message):
    hotkeys.altF4()

@dp.message_handler(text_contains="ScreenShot")
async def screenShot(message: types.Message):
    if admin_id == message.chat.id:
        screenshot.screenshot(message)

@dp.message_handler(text_contains="Отменить таймер")
async def taimerStop(message: types.Message):
    if admin_id == message.chat.id:
        control.shutdown()
        await message.answer("✅")

@dp.message_handler(text_contains="Log out from user")
async def winL(message: types.Message):
    hotkeys.winL()

@dp.message_handler(text_contains="Reboot")
async def reboot(message: types.Message):
    if admin_id == message.chat.id:
        control.reboot()


class TimerW(StatesGroup):
    writeTimer = State()
    msgbox1 = State()


@dp.message_handler(text_contains="Таймер на выключение")
async def taimerOff(message: types.Message):
    await message.answer("Введите кол-во секунд по истечению которых пк выключится:")
    await TimerW.writeTimer.set()


@dp.message_handler(state=TimerW.writeTimer)
async def taimer2Off(message: types.Message, state: FSMContext):
    await state.update_data(wiritedTimer=message.text)
    tmer = await state.get_data()
    await state.finish()
    os.system(f'shutdown /s /t {tmer["wiritedTimer"]}')


@dp.message_handler(text_contains="Сообщение на экран")
async def MsgBox(message: types.Message):
    await message.answer("Введите текст:")
    await TimerW.msgbox1.set()


@dp.message_handler(state=TimerW.msgbox1)
async def msgBox(message: types.Message, state: FSMContext):
    await state.update_data(WritedText=message.text)
    msg = await state.get_data()
    await state.finish()
    easygui.msgbox(f"{msg['WritedText']}", "PC_Control")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    executor.on_startup()