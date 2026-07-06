import asyncio

from vinted_hunter.app import Application


async def main():
    app = Application()
    await app.run_once()


if __name__ == "__main__":
    asyncio.run(main())