from aiogram import types

# -- Start menu
main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons1 = ["Media", "Hotkeys", "Controls",
            "Screen", "Game Controls"]
main_keyboard.add(*buttons1)

# -- Media menu
media_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons2 = ["🔊", "🔇", "🔉",
           "⏪", "⏯", "⏩",
           " ", "⬆️", " ",
           "⬅️", "⬇️", "➡️",
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

# -- Screen menu
screen_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons5 = ["Screenshot",
            "🔙 Back"]
screen_keyboard.add(*buttons5)

# -- Game Controls menu
game_ctrl_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons7 = ["Open Rust", "Connect to server",
            "🔙 Back"]
game_ctrl_keyboard.add(*buttons7)

cntlScreen_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons6 = []