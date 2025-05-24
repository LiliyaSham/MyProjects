import asyncio

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.enums import ChatAction

import app.keyboards as kb

router = Router()

@router.message(CommandStart())         
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id, action=ChatAction.TYPING)
    await asyncio.sleep(2)
    await message.answer('Welcome!', reply_markup=ReplyKeyboardRemove())

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(f'{message.from_user.first_name}, вам нужна помощь?', reply_markup=kb.inline_main)
 #   await message.answer(f'Ваш ID: {message.from_user.id}')

@router.message(F.text == "Как дела?")
async def how_are_you(message: Message):
    await message.answer('OK!')

@router.message(F.photo)
async def handle_photo(message: Message):
    file_id = message.photo[-1].file_id
    await message.answer_photo(file_id, caption='Вот твое фото')

@router.message(F.video)
async def handle_video(message: Message):
    file_id = message.video.file_id
    await message.answer_video(file_id, caption='Here is your video')

@router.message(F.sticker)
async def handle_sticker(message: Message):
    file_id = message.sticker.file_id
    await message.answer_sticker(file_id)

@router.message(F.text == 'проверка роутера')
async def check_router(message: Message):
    await message.answer('все ок')