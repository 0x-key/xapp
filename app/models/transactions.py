""" Expense Model """
from typing import Optional
from datetime import datetime, date
from enum import StrEnum, auto

from pydantic import BaseModel

from .expenses import ExpenseCategory
from .incomes import IncomeCategory


class TransactionType(StrEnum):
    """ Transaction Type """
    credit = auto()
    debit = auto()


class PreTransaction(BaseModel):
    """ Pre Transaction Record """
    transaction_type: TransactionType
    category: IncomeCategory | ExpenseCategory
    transaction_date: datetime | date
    issuer: str
    description: Optional[str]
    amount: float


class CreditPreTransaction(PreTransaction):
    """ Credit Pre Transaction Model """
    transaction_type: Optional[TransactionType] = TransactionType.credit
    category: IncomeCategory

class DebitPreTransaction(PreTransaction):
    """ Debit Pre Transaction Model """
    transaction_type: Optional[TransactionType] = TransactionType.debit
    category: ExpenseCategory

class TransactionId(BaseModel):
    """ Transaction Id Model """
    id: str

class Transaction(PreTransaction, TransactionId):
    """ Transaction Model """
    pass

class Transactions(BaseModel):
    """ List of Transactions Models """
    transactions: list[Transaction]
