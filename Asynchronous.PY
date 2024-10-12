import asyncio

async def hello():
    await asyncio.sleep(0)
    print("Hello")

async def world():
    await asyncio.sleep(2)
    print("World")

async def Sadiya():
    await asyncio.sleep(3)
    print("Sadiya")

async def Asad():
    await asyncio.sleep(2)
    print("Asad")

async def MP():
    await asyncio.sleep(0)
    print("MY PRECIOUS")
async def main():
    await asyncio.gather(hello(), world(),Sadiya(),Asad(),MP())

if __name__ == '__main__':
    asyncio.run(main())
