"""
Модуль с реализацией бизнес-логики.
"""
import gspread
from gspread import Worksheet
from typing import List, Any
from datetime import datetime, date

from utils.utils import make_right_date_format


def _get_worksheet(sheet_num: int) -> Worksheet:
    gc = gspread.service_account(
        filename='E:/vovasProgram/bot_with_google_sheets/services/mytestpythonproject-394706-4cc29a499b41.json'
    )
    sh = gc.open("Test_table")
    return sh.get_worksheet(sheet_num)


def _create_text(input_table: List[dict]) -> str:
    result: str = ''

    for row in input_table:
        text_row: str = ''
        for elem in row:
            text_row += str(row[elem]) + '_'

        text_row = text_row[:-1] + '\n'
        result += text_row

    return result


def name_ticker_share() -> str:
    result_table: List[dict[str, Any]] = []
    worksheet: Worksheet = _get_worksheet(0)
    column_names: List[str] = ['Наименование', 'Тикер', 'Доля в портфеле']

    table: List[dict[str, Any]] = worksheet.get_all_records()

    for row in table:
        print(row)
        result_row: dict[str, Any] = dict()

        for key in column_names:
            result_row[key] = row[key]

        result_table.append(result_row)

    return _create_text(result_table)


def branch_share() -> str:
    result_table: List[dict[str, Any]] = []
    worksheet: Worksheet = _get_worksheet(1)
    column_names: List[str] = ['Отрасль', 'Доля']

    table: List[dict[str, Any]] = worksheet.get_all_records()

    for row in table:
        result_row: dict[str, Any] = dict()

        for key in column_names:
            result_row[key] = row[key]

        result_table.append(result_row)

    return _create_text(result_table)


def name_ticker_profit(dates: set[date], ranges: List[List[date]]) -> str:
    # Обозначим переменные
    result_table: List[dict[str, Any]] = []
    worksheet: Worksheet = _get_worksheet(2)
    column_names: List[str] = ['Дата', 'Наименование', 'Тикер', 'Доход в процентах']

    # Заполним таблицу необходимыми данными
    table: List[dict[str, Any]] = worksheet.get_all_records()

    for row in table:
        result_row: dict[str, Any] = dict()
        day: date = datetime.strptime(row['Дата'], "%d.%m.%Y").date()

        # Проверим, есть ли дата в таблице в выбранных диапазонах
        day_in_ranges: bool = False
        for span in ranges:
            if span[0] <= day <= span[1]:
                day_in_ranges = True
                break

        if (day in dates) or day_in_ranges:
            for key in column_names:
                result_row[key] = row[key]

        result_table.append(result_row)

    final_table = sorted(result_table, key=lambda d: d['Дата'])

    result_text: str = _create_text(final_table) + 'Всего доход %%: ' + str(worksheet.get('E2')[0][0])

    return result_text
