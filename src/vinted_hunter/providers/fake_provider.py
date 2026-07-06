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
                image_url="https://example.com/image1.jpg",
            ),
            Item(
                id="2",
                title="Adidas Samba",
                brand="Adidas",
                price=75.0,
                size="42",
                url="https://example.com/item/2",
                image_url="https://example.com/image2.jpg",
            ),
            Item(
                id="3",
                title="Puma Suede",
                brand="Puma",
                price=60.0,
                size="41",
                url="https://example.com/item/3",
                image_url="https://example.com/image3.jpg",
            ),
        ]