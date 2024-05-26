
class Display:
    def __init__(self, id, message="", is_on=False, car_park="Unknown"):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        carpark_info = f"Car Park at {location}, with {capacity}"
        return carpark_info