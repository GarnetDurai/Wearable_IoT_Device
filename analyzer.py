def analyze_data(data):
    """
    Analyzes sensor data and returns a status code.
    0 = Normal
    1 = Warning
    2 = Critical
    """

    heart_rate = data.get("heart_rate", 0)
    spo2 = data.get("spo2", 100)
    co_level = data.get("co_level", 0)
    air_quality = data.get("air_quality", 0)
    temperature = data.get("temperature", 30)

    # -------- CRITICAL --------
    if heart_rate > 130:
        return 2

    if spo2 < 90:
        return 2

    if co_level > 60:
        return 2

    if air_quality > 200:
        return 2

    if temperature > 40:
        return 2


    # -------- WARNING --------
    if heart_rate > 100:
        return 1

    if spo2 < 94:
        return 1

    if co_level > 45:
        return 1

    if air_quality > 130:
        return 1

    if temperature > 37:
        return 1


    # -------- NORMAL --------
    return 0