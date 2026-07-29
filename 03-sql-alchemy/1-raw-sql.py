from sqlalchemy import create_engine, text

# -----------------------------------
# Create Engine
# -----------------------------------

engine = create_engine(
    "sqlite:///03-sql-alchemy/database/raw_sql.db",
    echo=True
)

# -----------------------------------
# Connection
# -----------------------------------

connection = engine.connect()

# -----------------------------------
# Create Table
# -----------------------------------

connection.execute(
    text("""
        CREATE TABLE IF NOT EXISTS people(
            name TEXT,
            age INTEGER
        )
    """)
)

connection.commit()   # if no commit, then rollback

# -----------------------------------
# Insert using Connection
# -----------------------------------

connection.execute(
    text("""
        INSERT INTO people(name, age)
        VALUES ('Mike', 30)
    """)
)

connection.commit()

# -----------------------------------
# Insert Another Record
# -----------------------------------

connection.execute(
    text("""
        INSERT INTO people(name, age)
        VALUES ('Jane', 40)
    """)
)

connection.commit()

# -----------------------------------
# Select
# -----------------------------------

result = connection.execute(
    text("""
        SELECT * FROM people
    """)
)

print("\nPeople Table\n")

for row in result.fetchall():
    print(row)

# -----------------------------------
# Close Connection
# -----------------------------------

connection.close()