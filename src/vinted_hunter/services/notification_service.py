from vinted_hunter.telegram.client import send_message


class NotificationService:
    async def send_startup_message(self) -> None:
        await send_message(
            "🚀 Vinted Hunter started\n\n"
            "The application is running successfully."
        )