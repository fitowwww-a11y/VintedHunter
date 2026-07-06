from vinted_hunter.models.item import Item
from vinted_hunter.telegram.client import send_message


class NotificationService:
    async def send_items(self, items: list[Item]) -> None:
        if not items:
            await send_message("❌ Nothing found")
            return

        for item in items:
            await send_message(
                f"""🔥 {item.title}

🏷 Brand: {item.brand}
💰 Price: {item.price} PLN
📏 Size: {item.size}

{item.url}
"""
            )