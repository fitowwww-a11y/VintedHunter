import asyncio

from vinted_hunter.core.logger import app_logger
from vinted_hunter.services.notification_service import NotificationService


async def main():
    app_logger.info("Starting application...")

    notifications = NotificationService()
    await notifications.send_startup_message()

    app_logger.info("Application started successfully")


if __name__ == "__main__":
    asyncio.run(main())
    notifications = NotificationService()
    from vinted_hunter.config.settings import settings

print(settings.telegram_bot_token)
print(settings.telegram_chat_id)