""" HTTP REST API """
from fastapi import FastAPI

from .internal.constants import api_version
from .routers import transactions, health

app = FastAPI(
    title="Mr. X xpenses",
    version=api_version,
    prefix="/v0",
    contact={
        "name": "Mr. X",
        "github": "https://github.com/0x-key",
    },
)

app.include_router(health.router)
app.include_router(transactions.router)
