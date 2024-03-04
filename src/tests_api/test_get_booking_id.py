import pytest
import requests
import aiohttp
import asyncio

from config import TEST_URL


@pytest.mark.asyncio
async def test_get_existing_booking():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{TEST_URL}") as response_get:
            get_all_bookings = await response_get.json()
            async with session.get(f"{TEST_URL}{get_all_bookings[0]['bookingid']}") as response:
                assert response.status == 200
                booking = await response.json()
                assert booking


def test_get_nonexistent_booking():
    nonexistent_booking_id = "X"
    response = requests.get(f"{TEST_URL}{nonexistent_booking_id}")
    assert response.status_code == 404
