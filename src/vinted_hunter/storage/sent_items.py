from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]

DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

FILE = DATA_DIR / "sent_items.txt"


class SentItemsStorage:

    def __init__(self):
        FILE.touch(exist_ok=True)

    def load(self) -> set[str]:
        return set(FILE.read_text().splitlines())

    def save(self, item_id: str):
        with FILE.open("a") as f:
            f.write(item_id + "\n")