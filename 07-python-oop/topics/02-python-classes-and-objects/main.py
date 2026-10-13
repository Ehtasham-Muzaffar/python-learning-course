"""Python classes and objects: independent learner project. See README.md for purpose and use."""

class Sensor:
    def __init__(self, name: str, reading: float) -> None:
        self.name = name
        self.reading = reading

sensor = Sensor("temperature", 21.5)
print(sensor.name, sensor.reading)
