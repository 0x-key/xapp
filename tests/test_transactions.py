""" Test Transaction Router """
from datetime import datetime
from app.models.expenses import ExpenseCategory
from app.models.transactions import TransactionType, TransactionId, PreTransaction, Transactions, Transaction
from .test_app import client

valid_transaction_id = None

def test_get_transactions_empty():
    """ Test get transactions when there isn't one registered. """
    response = client.get(
        url="/transactions",
    )
    assert response.status_code == 200
    transactions = Transactions(**response.json())
    assert len(transactions.transactions) == 0


def test_register_transaction():
    """ Test add transaction. """
    global valid_transaction_id
    response = client.post(
        url="/transactions",
        content=PreTransaction(
            transaction_type=TransactionType.debit,
            category=ExpenseCategory.gymnasium,
            transaction_date=datetime.now().isoformat(),
            issuer="Gym",
            amount=90,
            description=None,
        ).model_dump_json(),
    )
    assert response.status_code == 200
    response = TransactionId(**response.json())
    valid_transaction_id = response.id

def test_get_transaction():
    """ Test get transaction endpoint. """
    response = client.get(
        url="/transactions",
    )
    assert response.status_code == 200
    transactions = Transactions(**response.json())
    assert len(transactions.transactions) == 1

def test_get_transaction_by_id():
    response = client.get(
        url=f"/transactions/{valid_transaction_id}",
    )
    assert response.status_code == 200
    assert Transaction(**response.json())

def test_get_transaction_by_id_non_existent():
    transaction_id = "notregisteredtransactionid"
    response = client.get(
        url=f"/transactions/{transaction_id}",
    )
    assert response.status_code == 404
