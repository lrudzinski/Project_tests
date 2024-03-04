import pytest
import requests

from config import TEST_URL, get_authtoken


import pytest
import aiohttp
import asyncio


@pytest.mark.asyncio
async def test_delete_booking():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{TEST_URL}") as response_get:
            get_all_bookings = await response_get.json()
            booking_id = get_all_bookings[0]["bookingid"]
            async with session.delete(f"{TEST_URL}{booking_id}", cookies={"token": get_authtoken()}) as response:
                assert response.status == 201
