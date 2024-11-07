"""
Модуль с хэндлерами для пользователей с обычным статусом,
например, для тех, кто запустил бота в первый раз.
"""
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from datetime import date
from typing import List

import keyboards
from lexicon.lexicon_ru import LEXICON_RU
from services import services
from filters.other_filters import ShowTransactions


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


@router.message(ShowTransactions())
async def process_transaction_command(message: Message, dates: set[date], ranges: List[List[date]]):
    msg_text: str = services.name_ticker_profit(dates, ranges)
    await message.answer(text=msg_text)
