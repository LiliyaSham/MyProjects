import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

dp = Dispatcher()


@dp.message(Command("help"))
@dp.message(Command("help1"))
@dp.message(Command("start"))
async def echo_handler(message: types.Message) -> None:
    await message.answer('answer')
    await message.reply("reply")
    await asyncio.sleep(3)
#    await message.send_copy(chat_id=message.chat.id)


async def main() -> None:
    token = "..."
    bot = Bot(token)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
