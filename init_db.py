from database import get_db_connection

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Drop the table if it exists to ensure schema update
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

if __name__ == "__main__":
    init_db()
