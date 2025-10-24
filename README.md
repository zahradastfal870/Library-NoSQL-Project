
# 📚 Library Graph Project — Cassandra & Neo4j Integration

## 🧩 Overview
This project demonstrates how to integrate two different NoSQL databases:

- 🧱 **Apache Cassandra** — for structured data storage (wide-column store)  
- 🕸 **Neo4j** — for graph-based visualization and relationships

The use case is a simple **Library Management System** that manages:
- 👤 Users  
- 📘 Books  
- 🔄 Borrow transactions

---

## ⚙️ Requirements
- Python 3.11 ✅
- Docker Desktop 🐳
- PowerShell or Terminal
- PyCharm (or VS Code)
- Cassandra & Neo4j Docker images

---

## 🐳 Step 1: Run Cassandra with Docker
```bash
docker run --name cassandra -p 9042:9042 -d cassandra:latest
docker ps   # check if the container is running
````

---

## 🧠 Step 2: Connect to Cassandra and Create Schema

```bash
docker exec -it cassandra cqlsh
```

```sql
CREATE KEYSPACE library_ks WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
USE library_ks;

CREATE TABLE users (user_id text PRIMARY KEY, name text);
CREATE TABLE books (isbn text PRIMARY KEY, title text);
CREATE TABLE borrows (user_id text, isbn text, borrowed_at timestamp, PRIMARY KEY(user_id, isbn));
```

---

## 📥 Step 3: Insert Sample Data

```sql
-- Users
INSERT INTO users (user_id, name) VALUES ('u1', 'Zahra');
INSERT INTO users (user_id, name) VALUES ('u2', 'Noah');
INSERT INTO users (user_id, name) VALUES ('u3', 'Mina');

-- Books
INSERT INTO books (isbn, title) VALUES ('isbn123', 'Python Basics');
INSERT INTO books (isbn, title) VALUES ('isbn456', 'Data Structures in Python');
INSERT INTO books (isbn, title) VALUES ('isbn789', 'NoSQL with Cassandra & Neo4j');

-- Borrows
INSERT INTO borrows (user_id, isbn, borrowed_at) VALUES ('u1', 'isbn123', toTimestamp(now()));
INSERT INTO borrows (user_id, isbn, borrowed_at) VALUES ('u2', 'isbn456', toTimestamp(now()));
INSERT INTO borrows (user_id, isbn, borrowed_at) VALUES ('u3', 'isbn789', toTimestamp(now()));

-- Check data
SELECT * FROM users;
SELECT * FROM books;
SELECT * FROM borrows;
```

---

## 🐍 Step 4: Create and Activate Python Virtual Environment

```bash
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install cassandra-driver neo4j
```

---

## 🧠 Step 5: Connect to Neo4j & Create Graph

```python
# test_connection.py
from db.neo4j_client import Neo4jClient

client = Neo4jClient(uri="bolt://localhost:7687", user="neo4j", password="12345678")

result = client.create_user(user_id="u1", name="Zahra")
print("User created:", result)

result = client.create_book(isbn="isbn123", title="Python Basics")
print("Book created:", result)

result = client.relate_borrow(user_id="u1", isbn="isbn123")
print("Relation created:", result)

client.close()
```

---

## 🧪 Step 6: Test Cassandra in Python

```python
# test_cassandra.py
from db.cassandra_client import CassandraClient

client = CassandraClient(keyspace="library_ks")
print("Users:", client.get_users())
print("Books:", client.get_books())
print("Borrows:", client.get_borrows())
client.close()
```

---

## 🕸 Step 7: View Graph in Neo4j Browser

Open in your browser:

```
http://localhost:7474
```

Log in with:

```
Username: neo4j
Password: 12345678
```

You will see the graph of Users → Books (BORROWED relationships).

---

## ✅ Final Output

* ✅ Cassandra container running via Docker
* ✅ Neo4j database connected and visualized
* ✅ Python 3.11 virtual environment set up
* ✅ Data successfully inserted and retrieved
* ✅ Graph successfully displayed in Neo4j Browser

---

## 🖼 Screenshots Table

| Step | File Name                             | Description                  |
| ---- | ------------------------------------- | ---------------------------- |
| 1    | step1_project_structure.png           | Project structure in PyCharm |
| 2    | step2_neo4j_db_created.png            | Neo4j DB created             |
| 3    | step3_neo4j_constraints.png           | Neo4j constraints            |
| 4    | step4_neo4j_client_code.png           | Neo4j client Python code     |
| 5    | step5_test_neo4j_py_output.png        | Neo4j test output            |
| 6    | step6_seed_run.png                    | Seeding data                 |
| 7    | step7_neo4j_graph_with_relations.png  | Graph visualization          |
| 8    | step8_docker_ok.png                   | Docker running               |
| 9    | step9_cassandra_container_running.png | Cassandra container running  |
| 10   | step10_cqlsh_open.png                 | CQLSH opened                 |
| 11   | step11_cassandra_schema_created.png   | Schema created               |
| 12   | step12_cassandra_sample_data.png      | Sample data inserted         |
| 13   | step13_cassandra_select_test.png      | SELECT test                  |
| 14   | step14_test_cassandra_py_output.png   | Cassandra Python output      |

---

## 🧾 Tech Stack

* 🐍 **Language:** Python 3.11
* 🧱 **Databases:** Cassandra & Neo4j
* 🐳 **Tools:** Docker, PowerShell, PyCharm
* 📦 **Libraries:** cassandra-driver, neo4j

---

## ✍️ Author

👩 **Zahra Dastfal**
📚 University of Central Missouri

