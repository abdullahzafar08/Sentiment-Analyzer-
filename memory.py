import os
import sqlite3
import json
from typing import Optional

DB_PATH = os.path.join(os.path.dirname(__file__), "memory.db")


class MemoryStore:
    """Simple key-value store backed by sqlite. Provides explicit methods
    to save and retrieve the last user input. This is used as a reliable
    fallback even if `mem0` isn't installed.
    """

    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self._init_table()

    def _init_table(self):
        cur = self.conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS kv (
                k TEXT PRIMARY KEY,
                v TEXT,
                updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        self.conn.commit()

    def set(self, key: str, value) -> None:
        v = json.dumps(value)
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO kv(k, v) VALUES (?, ?)"
            " ON CONFLICT(k) DO UPDATE SET v=excluded.v, updated=CURRENT_TIMESTAMP",
            (key, v),
        )
        self.conn.commit()

    def get(self, key: str) -> Optional[object]:
        cur = self.conn.cursor()
        cur.execute("SELECT v FROM kv WHERE k = ?", (key,))
        row = cur.fetchone()
        if not row:
            return None
        try:
            return json.loads(row[0])
        except Exception:
            return row[0]

    def close(self):
        try:
            self.conn.close()
        except Exception:
            pass

    # Convenience helpers for this project
    def set_last_user_input(self, text: str) -> None:
        self.set("last_user_input", {"text": text})

    def get_last_user_input(self) -> Optional[dict]:
        return self.get("last_user_input")


def get_memory_store() -> MemoryStore:
    # If mem0 is installed, callers could extend this to use mem0 APIs.
    # For now we return the sqlite-backed MemoryStore for reliability.
    return MemoryStore()
