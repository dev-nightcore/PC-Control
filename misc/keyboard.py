from aiogram import types

# -- Start menu
main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons1 = ["Media control", "Hotkeys"
           "Отменить таймер", "Перезагрузка", "Таймер на выключение",
           "ScreenShot", "Сообщение на экран"]
main_keyboard.add(*buttons1)

# -- Media menu
media_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons2 = ["🔊", "🔇", "🔉",
           "⏪", "⏯", "⏩",
           "🔙 Back"]
media_keyboard.add(*buttons2)

# -- Hotkey menu
hotkey_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons3 = ["ALT+TAB", "ALT+F4",
            "🔙 Back"]
hotkey_keyboard.add(*buttons3)

# -- Control pc menu
control_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons4 = ["Reboot", "Shutdown",
            "Log out from user",
            "🔙 Back"]
control_keyboard.add(*buttons4)