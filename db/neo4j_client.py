from neo4j import GraphDatabase

class Neo4jClient:
    def __init__(self, uri="bolt://localhost:7687", user="neo4j", password="12345678"):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    # --- User CRUD ---
    def create_user(self, user_id, name):
        q = "MERGE (u:User {user_id:$user_id}) SET u.name=$name RETURN u"
        with self.driver.session() as s:
            return s.run(q, user_id=user_id, name=name).single()

    def get_user(self, user_id):
        q = "MATCH (u:User {user_id:$user_id}) RETURN u"
        with self.driver.session() as s:
            return s.run(q, user_id=user_id).single()

    # --- Book CRUD ---
    def create_book(self, isbn, title):
        q = "MERGE (b:Book {isbn:$isbn}) SET b.title=$title RETURN b"
        with self.driver.session() as s:
            return s.run(q, isbn=isbn, title=title).single()

    # --- Relation ---
    def relate_borrow(self, user_id, isbn):
        q = """
        MATCH (u:User {user_id:$user_id}), (b:Book {isbn:$isbn})
        MERGE (u)-[r:BORROWED]->(b)
        RETURN r
        """
        with self.driver.session() as s:
            return s.run(q, user_id=user_id, isbn=isbn).single()
