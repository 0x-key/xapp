""" Testing main.py """
import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app

@pytest.mark.anyio
async def test_hello_x():
    """ Test hello x endpoint. """
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == { "Hello": "Mr. X"}
