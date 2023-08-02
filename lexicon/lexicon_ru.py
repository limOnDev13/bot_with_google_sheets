"""
Модуль со словарем соответствий данных текстам на рус языке.
"""
LEXICON_COMMANDS_RU: dict[str, str] = {
    '/help': 'Справка о боте',
    '/name': 'Наименование_Тикер_Доля',
    '/branch': 'Отрасль_Доля',
    '/transactions': 'Наименование_Тикер_Доход'
}


LEXICON_RU: dict[str, str] = {
    'label_premium': 'Оплата товара',
    'label_discount': 'Скидка',
    'payment_title': 'Название товара',
    'payment_description': 'Описание оплаты',
    'payment_payload': 'Payment through a bot',
    'successful_payment_msg': 'Спасибо за оплату',
    'help': 'Данный бот выводит информацию о портфелях ценных бумаг'
            ' и сделках.\n/name - бот выведет портфель ценных бумаг'
            ' формате "Наименование_Тикер_Доля в портфеле".\n/branch - бот'
            ' выведет портфель в формате "Отрасль_Доля".\n/transaction '
            'дата1, дата2, дата3:дата4 - бот выведет сделки в формате '
            '"Наименование_Тикер_Доход в процентах", а также выведет'
            ' "Всего доход %%". Даты вводятся в формате ДД.ММ.ГГГГ'
            ' (если вести в формате ДД.ММ, то год будет текущим, '
            'если ввести просто ДД, то год и месяц будут текущими). Можно'
            ' вводить даты через запятую - данные будут выводиться'
            ' на эти даты, можно указать диапазон через : (между датами не должно быть'
            ' пробелов! Дата1:Дата2), тогда будет выведена информация о сделках в каждый день между введенными '
            'датами, включая эти самые даты'
}
