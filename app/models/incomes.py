""" Income Categories Model """
from enum import StrEnum, auto

class IncomeCategory(StrEnum):
    salary = auto()
    business = auto()
    investment = auto()
    rental = auto()
    capital_gains = auto()
    freelance = auto()
    pension = auto()
    government_transfers = auto()
    gifts = auto()
    debt_recovery = auto()
    royalties = auto()
    alimony = auto()
    side_hustle = auto()
    other = auto()
