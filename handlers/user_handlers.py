"""
Модуль с хэндлерами для пользователей с обычным статусом,
например, для тех, кто запустил бота в первый раз.
"""
from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, CallbackQuery
import keyboards
from lexicon.lexicon_ru import LEXICON_RU
import services


router: Router = Router()


# Обработка команды /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    # Отправим пользователю справку о боте
    await message.answer(text=LEXICON_RU['help'])
