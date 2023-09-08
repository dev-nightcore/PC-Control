async def send_live(chat_id: int):
    try:
        os.remove("s.png")
        await utils.screenshot()
        a = await bot.send_photo(chat_id ,open("s.png", "rb"), reply_markup=markup.live(), caption=f"📸 Live screeen")
        os.remove("s.png")
        while is_running:
            await utils.screenshot()
            new_photo = types.InputMediaPhoto(media=open("s.png", "rb"))
            await a.edit_caption(f"📸 Live screen")
            await a.edit_media(
                media=new_photo,
                reply_markup=markup.live(),
            )
            os.remove("s.png")
            await asyncio.sleep(0.8)
except FileNotFoundError:
        await utils.screenshot()
        a = await bot.send_photo(chat_id ,open("s.png", "rb"), reply_markup=markup.live(), caption=f"📸 Скриншот №{co}")
        os.remove("s.png")
        while is_running:
            await utils.screenshot()
            new_photo = types.InputMediaPhoto(media=open("s.png", "rb"))
            await a.edit_caption(f"📸 Скриншот №{co}")
            await a.edit_media(
                media=new_photo,
                reply_markup=markup.live(),
            )
            os.remove("s.png")
            await asyncio.sleep(0.8)
