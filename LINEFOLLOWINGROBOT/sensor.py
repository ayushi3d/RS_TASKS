def get_sensor_values():
    values = input("Enter 6 sensor values (e.g. 001100): ")

    sensors = list(map(int, values))

    active = len(list(filter(lambda x: x == 1, sensors)))

    return sensors, active