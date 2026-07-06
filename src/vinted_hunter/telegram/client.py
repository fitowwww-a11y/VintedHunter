from telegram import Bot

from vinted_hunter.config.settings import settings


async def send_message(text: str) -> None:
    bot = Bot(token=settings.telegram_bot_token)

    await bot.send_message(
        chat_id=settings.telegram_chat_id,
        text=text,
    )