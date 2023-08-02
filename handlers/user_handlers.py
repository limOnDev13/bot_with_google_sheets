"""
Модуль с хэндлерами для пользователей с обычным статусом,
например, для тех, кто запустил бота в первый раз.
"""
from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, CallbackQuery
import keyboards
from lexicon.lexicon_ru import LEXICON_RU
from services import services


router: Router = Router()


# Обработка команды /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    # Отправим пользователю справку о боте
    await message.answer(text=LEXICON_RU['help'])


@router.message(Command(commands='name'))
async def process_name_command(message: Message):
    msg_text: str = services.name_ticker_share()
    await message.answer(text=msg_text)


@router.message(Command(commands='branch'))
async def process_name_command(message: Message):
    msg_text: str = services.branch_share()
    await message.answer(text=msg_text)
