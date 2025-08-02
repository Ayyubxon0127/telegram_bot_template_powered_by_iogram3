from aiogram import types, Dispatcher
from aiogram.filters import Command
from keyboards.reply import main_menu_keyboard

def register_start_handlers(dp: Dispatcher):
    @dp.message(Command("start"))
    async def start_handler(message: types.Message):
        await message.answer(
            text="Assalomu alaykum!\nBu bot test rejimida ishlamoqda.",
            reply_markup=main_menu_keyboard()
        )

    @dp.message(lambda msg: msg.text == "📋 Mening Profilim")
    async def profile_handler(message: types.Message):
        user = message.from_user
        await message.answer(
            f"Sizning profilingiz:\n🆔 ID: <code>{user.id}</code>\n👤 Username: @{user.username}"
        )

    @dp.message(lambda msg: msg.text == "ℹ️ Yordam")
    async def help_handler(message: types.Message):
        await message.answer(
            "Yordam kerak bo‘lsa, bu yerga murojaat qiling: @admin_username"
        )
