import sqlite3

conn = sqlite3.connect("flight.db")
cursor = conn.cursor()
# 3️⃣ Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS flight (
    flightId INTEGER PRIMARY KEY,
    source TEXT NOT NULL,
    destination TEXT,
    noofseats INTEGER,
    flightfare REAL
);
""") 

# Insert data
cursor.execute("""
INSERT INTO flight (flightId, source, destination, noofseats, flightfare)
VALUES (?, ?, ?, ?, ?)
""", (18224, "Dubai", "Kochi", 25, 50000.0))

conn.commit()
conn.close()
