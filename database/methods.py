"""
Модуль содержит методы для работы с бд
"""
from . connection_pool import DataBaseClass


# Метод для фиксирования оплаты премиума
async def set_premium(connector: DataBaseClass, user_id: int):
    pass
