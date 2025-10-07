import json
from datetime import datetime
from tkinter.font import names


# Исключения
class CurrencyMismatchError(Exception):
    """Ошибка валюты при проведении операции."""
    pass

class InsufficientFundsError(Exception):
    """Ошибка: недостаточно средств при снятии."""
    pass

class AccountAlreadyExistsError(Exception):
    """Ошибка: счёт в данной валюте уже существует."""
    pass

class ClientAlreadyExistsError(Exception):
    """Ошибка: такой клиент уже существует."""
    pass

class AccountNotFound(Exception):
    """Ошибка: счёт в этой валюте не найден."""
    pass

class ClientNotFoundError(Exception):
    """Ошибка: такого клиента не существует."""
    pass

class Client:
    def __init__(self, client.id, name):
        self.client_id = client_id
        self.name = names
        self.client = {}





