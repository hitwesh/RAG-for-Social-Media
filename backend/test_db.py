import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    port=5433,
    user="postgres",
    password="postgres",
    database="videorag"
)

print("CONNECTED")

conn.close()