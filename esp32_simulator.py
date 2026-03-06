import requests
import random
import time

SERVER_URL = "http://localhost:5000/update"

while True:

    # Randomly choose system state
    mode = random.choice(["safe", "warning", "critical"])

    if mode == "safe":

        data = {
            "device_id": "esp32_simulator",
            "heart_rate": random.randint(70, 90),
            "spo2": random.randint(96, 100),
            "temperature": round(random.uniform(36.2, 37.2), 1),
            "co_level": random.randint(5, 15),
            "air_quality": random.randint(50, 90),
            "accel_x": round(random.uniform(-0.2, 0.2), 2),
            "accel_y": round(random.uniform(-0.2, 0.2), 2),
            "accel_z": round(random.uniform(0.9, 1.1), 2)
        }

    elif mode == "warning":

        data = {
            "device_id": "esp32_simulator",
            "heart_rate": random.randint(101, 115),
            "spo2": random.randint(92, 95),
            "temperature": round(random.uniform(38.0, 38.5), 1),
            "co_level": random.randint(25, 40),
            "air_quality": random.randint(120, 180),
            "accel_x": round(random.uniform(-0.5, 0.5), 2),
            "accel_y": round(random.uniform(-0.5, 0.5), 2),
            "accel_z": round(random.uniform(0.7, 1.3), 2)
        }

    else:  # CRITICAL

        data = {
            "device_id": "esp32_simulator",
            "heart_rate": random.randint(131, 150),
            "spo2": random.randint(80, 89),
            "temperature": round(random.uniform(39.5, 40.5), 1),
            "co_level": random.randint(55, 80),
            "air_quality": random.randint(210, 260),
            "accel_x": round(random.uniform(-1, 1), 2),
            "accel_y": round(random.uniform(-1, 1), 2),
            "accel_z": round(random.uniform(0.3, 1.8), 2)
        }

    try:
        response = requests.post(SERVER_URL, json=data)

        print("MODE:", mode.upper())
        print("Sent:", data)
        print("Server Response:", response.json())
        print("-----------------------------------")

    except Exception as e:
        print("Error:", e)

    time.sleep(2)