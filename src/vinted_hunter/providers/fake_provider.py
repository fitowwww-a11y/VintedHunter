from vinted_hunter.models.item import Item
from vinted_hunter.providers.base import SearchProvider


class FakeProvider(SearchProvider):
    async def search(self) -> list[Item]:
        return [
            Item(
                id="1",
                title="Nike Air Max 95",
                brand="Nike",
                price=180.0,
                size="43",
                url="https://example.com/item/1",
                image_url="https://example.com/image.jpg",
            )
        ]