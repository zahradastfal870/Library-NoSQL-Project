# db/cassandra_client.py
import os

# Force pure Python mode and asyncio loop (required for Python 3.12)
os.environ["CASS_DRIVER_NO_EXTENSIONS"] = "1"
os.environ["CASS_DRIVER_EVENT_LOOP_MANAGER"] = "asyncio"

from cassandra.cluster import Cluster
from cassandra.io.asyncorereactor import AsyncoreConnection
from cassandra.query import SimpleStatement


class CassandraClient:
    def __init__(self, hosts=None, port=9042, keyspace="library_ks"):
        self.hosts = hosts or ["127.0.0.1"]
        self.port = port
        self.keyspace = keyspace

        self.cluster = Cluster(
            contact_points=self.hosts,
            port=self.port,
            connection_class=AsyncoreConnection
        )
        self.session = self.cluster.connect(self.keyspace)

    def close(self):
        if self.session:
            self.session.shutdown()
        if self.cluster:
            self.cluster.shutdown()

    def create_user(self, user_id, name):
        q = SimpleStatement("INSERT INTO users (user_id, name) VALUES (?, ?)")
        self.session.execute(q, (user_id, name))

    def create_book(self, isbn, title):
        q = SimpleStatement("INSERT INTO books (isbn, title) VALUES (?, ?)")
        self.session.execute(q, (isbn, title))

    def create_borrow(self, user_id, isbn):
        q = SimpleStatement(
            "INSERT INTO borrows (user_id, isbn, borrowed_at) VALUES (?, ?, toTimestamp(now()))"
        )
        self.session.execute(q, (user_id, isbn))

    def get_users(self):
        return list(self.session.execute("SELECT * FROM users"))

    def get_books(self):
        return list(self.session.execute("SELECT * FROM books"))

    def get_borrows(self):
        return list(self.session.execute("SELECT * FROM borrows"))
