import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiohttp.web_fileresponse import content_type

from config import BOT_TOKEN
from handlers import start

async def main():
    ...
    dp = Dispatcher()

    # start.py dagi handlerlarni ulaymiz
    start.register_start_handlers(dp)


async def main():
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    @dp.message(Command("start"))
    async def start_handler(message: types.Message):
        kb = types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton(text="📋 Mening Profilim")],
                [types.KeyboardButton(text="ℹ️ Yordam")],
            ],
            resize_keyboard=True
        )
        await message.answer("Assalomu alaykum!\nBot ishga tushdi ✅", reply_markup=kb)

    @dp.message(lambda msg: msg.text == "📋 Mening Profilim")
    async def profile_handler(message: types.Message):
        user = message.from_user
        await message.answer(
            f"Sizning profilingiz:\n🆔 ID: <code>{user.id}</code>\n👤 Username: @{user.username}"
        )

    @dp.message(lambda msg: msg.text == "ℹ️ Yordam")
    async def help_handler(message: types.Message):
        await message.answer("Yordam uchun: @admin_username")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
