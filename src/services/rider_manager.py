from src.dataclasses.user import Rider


class RiderManager:

    def __init__(self):
        self.riders = {}

    def add(self, rider_id: str, x_coordinate: int, y_coordinate: int):
        self.riders[rider_id] = Rider(
            id=rider_id,
            x_coordinate=x_coordinate,
            y_coordinate=y_coordinate
        )

    def get_rider(self, rider_id: str) -> Rider:
        return self.riders.get(rider_id)
