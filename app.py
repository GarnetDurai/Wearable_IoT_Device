from flask import Flask, request, jsonify, render_template
from database import get_db_connection, init_db
from analyzer import analyze_data

app = Flask(__name__)

# Initialize DB on start (optional, or run init_db.py separately)
# For this refactor, we'll assume the user might want to run init_db() manually or we can check if table exists.
# But to ensure the schema is correct as per request, let's provide a route or just rely on the user running init_db.py.
# However, to be helpful, I will add a command line check or just leave it to init_db.py.

@app.route("/")
def home():
    return "Flask backend is running with upgraded sensor support!"

@app.route("/update", methods=["POST"])
def update():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    print("📥 Received JSON data:", data)

    # Analyze data to get status code
    status_code = analyze_data(data)
    
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sensor_readings (
            device_id, heart_rate, spo2, temperature, co_level, 
            air_quality, accel_x, accel_y, accel_z, status_code
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get("device_id"),
        data.get("heart_rate"),
        data.get("spo2"),
        data.get("temperature"),
        data.get("co_level"),
        data.get("air_quality"),
        data.get("accel_x"),
        data.get("accel_y"),
        data.get("accel_z"),
        status_code
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "status": "success",
        "status_code": status_code
    })

@app.route("/data", methods=["GET"])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM sensor_readings
        ORDER BY timestamp DESC
        LIMIT 20
    """)

    rows = cursor.fetchall()
    conn.close()

    data = []
    for row in rows:
        data.append(dict(row))

    return jsonify(data)

@app.route("/latest")
def latest():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM sensor_readings
        ORDER BY timestamp DESC
        LIMIT 1
    """)

    row = cursor.fetchone()
    conn.close()

    if row:
        return jsonify(dict(row))

    return jsonify({"error": "No data available"})

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
