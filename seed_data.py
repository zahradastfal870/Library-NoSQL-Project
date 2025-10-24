from db.neo4j_client import Neo4jClient

client = Neo4jClient(uri="bolt://localhost:7687", user="neo4j", password="12345678")

users = [("u1", "Zahra"), ("u2", "Noah"), ("u3", "Mina")]
books = [
    ("isbn123", "Python Basics"),
    ("isbn456", "Data Structures in Python"),
    ("isbn789", "NoSQL with Cassandra & Neo4j"),
]

# create users
for uid, name in users:
    r = client.create_user(uid, name)
    print("User:", uid, "->", r)

# create books
for isbn, title in books:
    r = client.create_book(isbn, title)
    print("Book:", isbn, "->", r)

# create borrow relations
relations = [("u1", "isbn456"), ("u2", "isbn123"), ("u3", "isbn789")]
for uid, isbn in relations:
    r = client.relate_borrow(uid, isbn)
    print("Borrow:", uid, "->", isbn, ":", r)

client.close()
print("Done seeding.")
