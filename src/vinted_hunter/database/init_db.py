from vinted_hunter.database.database import get_connection


def init_database() -> None:
    connection = get_connection()

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS items(
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            brand TEXT,
            price REAL,
            size TEXT,
            url TEXT,
            image_url TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    connection.commit()
    connection.close()