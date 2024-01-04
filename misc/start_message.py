from config import whitelisted_id, bot

async def send_message():
    await bot.send_message(
            whitelisted_id,
            text=f"<b>PC and bot started and ready to use</b>",
            parse_mode="HTML")