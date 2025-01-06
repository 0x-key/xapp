""" Transactions Router """
from uuid import uuid4

from fastapi import APIRouter, HTTPException

from app.models.transactions import Transactions, Transaction, TransactionId, CreditPreTransaction, \
    DebitPreTransaction

router = APIRouter(prefix="/transactions", tags=["Financial Transactions"])

fake_db: list[Transaction] = list()


@router.post(
    "",
    response_model=TransactionId,
    status_code=200,
)
async def register_transaction(pre_transaction: CreditPreTransaction | DebitPreTransaction):
    """ Register new transaction. """
    max_attempts = 500
    fake_db_index = [t.id for t in fake_db]
    attempts = 0
    transaction_id = None
    while transaction_id is None and attempts < max_attempts:
        temp_id = uuid4().hex
        if temp_id not in fake_db_index:  # Check if the generated ID is unique
            transaction_id = temp_id
        attempts += 1

    if transaction_id is None:
        raise HTTPException(status_code=409, detail="Pre-transaction process failed.")

    stored = Transaction(
        id=transaction_id,
        **pre_transaction.model_dump(),
    )
    fake_db.append(stored)
    return TransactionId(id=transaction_id)


@router.get(
    "",
    response_model=Transactions,
    status_code=200,
)
async def get_transactions():
    """ Get all transactions. """
    return Transactions(transactions=fake_db)


@router.get(
    "/{transaction_id}",
    response_model=Transaction,
    status_code=200,
)
async def get_transaction_by_id(transaction_id: str):
    """ Get transaction by id. """
    transaction = None
    for t in fake_db:
        if t.id == transaction_id:
            transaction = t
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found.")
    return transaction