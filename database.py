import sqlite3

DB_NAME = "sensor_data.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the database with the updated schema."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Drop the table if it exists to ensure schema update (WARNING: Deletes old data)
    # For a prototype, this is often acceptable to apply schema changes.
    # If you want to preserve data, you would need a migration script.
    cursor.execute("DROP TABLE IF EXISTS sensor_readings")

    cursor.execute("""
        CREATE TABLE sensor_readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT,
            heart_rate INTEGER,
            spo2 INTEGER,
            temperature REAL,
            co_level INTEGER,
            air_quality INTEGER,
            accel_x REAL,
            accel_y REAL,
            accel_z REAL,
            status_code INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()
    print("Database initialized with new schema.")
