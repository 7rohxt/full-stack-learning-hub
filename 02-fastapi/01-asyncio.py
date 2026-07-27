import asyncio

async def make_tea():
    print("Making tea...")
    await asyncio.sleep(3)
    print("Tea ready!")

async def toast_bread():
    print("Toasting bread...")
    await asyncio.sleep(2)
    print("Bread ready!")

# The below function is still synchronous (Without asyncio.gather)
async def main():     # --> this will take 5 secs (3+2)
    await make_tea()
    await toast_bread() 

# The below fuction uses asyncio (with gather)
async def main():     # --> the below function will only take 3 secs.
    await asyncio.gather(
        make_tea(),
        toast_bread()
    )

asyncio.run(main())