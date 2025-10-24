# test_cassandra.py
from db.cassandra_client import CassandraClient

client = CassandraClient(keyspace="library_ks")

print("Users:", client.get_users())
print("Books:", client.get_books())
print("Borrows:", client.get_borrows())

client.close()
