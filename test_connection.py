from db.neo4j_client import Neo4jClient

# Create connection
client = Neo4jClient(uri="bolt://localhost:7687", user="neo4j", password="12345678")

# Test creating a user
result = client.create_user("u1", "Zahra")
print("User created:", result)

# Test creating a book
result = client.create_book("isbn123", "Python Basics")
print("Book created:", result)

# Test creating a relationship between user and book
result = client.relate_borrow("u1", "isbn123")
print("Relation created:", result)

# Close the connection
client.close()
