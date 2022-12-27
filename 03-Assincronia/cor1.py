import asyncio

async def oi():
    print('Oi')


el = asyncio.get_event_loop()
el.run_until_complete(oi())
el.close()