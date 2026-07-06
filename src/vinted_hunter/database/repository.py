from vinted_hunter.database.database import get_connection
from vinted_hunter.models.item import Item


class ItemRepository:
    def exists(self, item_id: str) -> bool:
        connection = get_connection()

        row = connection.execute(
            "SELECT 1 FROM items WHERE id = ?",
            (item_id,),
        ).fetchone()

        connection.close()

        return row is not None

    def save(self, item: Item) -> None:
        connection = get_connection()

        connection.execute(
            """
            INSERT INTO items(
                id,
                title,
                brand,
                price,
                size,
                url,
                image_url
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                item.id,
                item.title,
                item.brand,
                item.price,
                item.size,
                item.url,
                item.image_url,
            ),
        )

        connection.commit()
        connection.close()