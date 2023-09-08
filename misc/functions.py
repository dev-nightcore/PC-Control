import time

from main import bot
# -- Functions


async def deleteMessage(message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

async def deleteBotMessage(bot_message):
    await bot.delete_message(chat_id=bot_message.chat.id, message_id=bot_message.message_id)

async def answerSucsessAndDelete(message):
        bot_message = await message.answer("✅")
        bot_message
        time.sleep(1)
        await bot.delete_message(chat_id=bot_message.chat.id, message_id=bot_message.message_id)