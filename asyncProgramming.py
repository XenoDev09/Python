import asyncio

async def main():
    await fun()

async def fun():
    print("Hello, Asyncio!")

asyncio.run(main())