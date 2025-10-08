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
    def __init__(self, client_id, name):
        self.client_id = client_id
        self.name = name
        self.client = {}

    def add_account(selfself, account_id)
        if account.currency in self.accounts
            raise AccountAlreadyExistsError(f"счет в валюте {account.currency} уже существует")
        self.accounts[account.currency] = account_id

    def remove_account(self, currency):
        if currency not in self.accounts:
            raise AccoundNotFound(f"счет в валюте {currency} не найден")
        def self.accounts[currency]

    def get_account(self,currency):
        if currency not in self.accounts:
            raise AccoundNotFound(f"счет в валюте {currency} не найден")
        self.accounts[currency] = currency

    def get all_accounts(self):
        return list(self.accounts.values())

def get all_account


