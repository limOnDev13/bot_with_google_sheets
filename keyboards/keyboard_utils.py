"""
Вспомогательные функции / методы, помогающие формировать клавиатуры.
"""
from aiogram.utils.keyboard import (ReplyKeyboardBuilder,
                                    KeyboardButton,
                                    ReplyKeyboardMarkup,
                                    InlineKeyboardBuilder)
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from asyncpg import Record
from typing import List
from datetime import time, date

from lexicon import LEXICON_RU
