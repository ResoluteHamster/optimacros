import aiohttp
import pytest

PORT = 80


async def calc_factorial(value: int):
    timeout = aiohttp.ClientTimeout(total=600)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.ws_connect(f'http://localhost:{PORT}/ws/factorial/') as ws:
            await ws.send_json(f'{{"request_factorial": "{value}"}}')
            result_json = await ws.receive_json()
            return result_json.get('result')


@pytest.mark.asyncio
async def test_factorial_zero():
    res = await calc_factorial(0)
    assert res == '1.0000000000000000E+00'


@pytest.mark.asyncio
async def test_factorial_first():
    res = await calc_factorial(10000)
    assert res == '2.8462596809170545E+35659'


@pytest.mark.asyncio
async def test_factorial_negative_int():
    res = await calc_factorial(-5)
    assert res.lower().find('error') >= 0


@pytest.mark.asyncio
async def test_factorial_str():
    res = await calc_factorial('lsdfkij')
    assert res.lower().find('error') >= 0

