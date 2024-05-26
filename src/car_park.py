
class CarPark:
    def __init__(self, location="Unknown", capacity="Unknown", plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.sensors = sensors or []  # uses the first value if not None, otherwise uses the second value
        self.plates = plates or []
        self.displays = displays

    def __str__(self):
        carpark_info = f"Car Park at {location}, with {capacity}"
        return carpark_info