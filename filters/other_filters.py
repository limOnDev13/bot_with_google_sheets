"""
Фильтры, которые не попали в другие файлы
"""
from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from typing import List, Any
from datetime import date

from utils import utils
from lexicon import LEXICON_RU


class ShowTransactions(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, set[date]]:
        words: List[str] = message.text.split(' ')

        if words[0] != '/transactions':
            return False

        words.pop(0)
        # Переведем введенные даты в тип datetime
        dates: set[date] = set()
        ranges: List[List[date]] = []

        for str_date in words:
            if '-' in str_date:
                try:
                    str_date_range: List[str] = str_date.split('-')
                    start_date: date = utils.make_right_date_format(str_date_range[0])
                    end_date: date = utils.make_right_date_format(str_date_range[1])
                    ranges.append([start_date, end_date])
                except ValueError:
                    await message.answer(text=LEXICON_RU['wrong_date_format'])
            else:
                try:
                    day: date = utils.make_right_date_format(str_date)

                    dates.add(day)
                except ValueError:
                    await message.answer(text=LEXICON_RU['wrong_date_format'])

        # Проверим, чтобы не было дублирования дат в диапазонах и множестве дат
        _dates_for_removing: set[date] = set()
        for span in ranges:
            for day in dates:
                if span[0] <= day <= span[1]:
                    _dates_for_removing.add(day)

        for item in _dates_for_removing:
            dates.remove(item)

        # Если множество пустое, то отклонить
        if (not len(dates)) and (not len(ranges)):
            return False
        else:
            return {'dates': dates,
                    'ranges': ranges}
