from typing import List

from src.constants import MAX_DISTANCE_SEARCH
from src.dataclasses.user import Driver
from src.helper import calculate_distance


class DriverManager:

    def __init__(self):
        self.drivers = {}

    def add(self, driver_id: str, x_coordinate: int, y_coordinate: int) -> None:
        self.drivers[driver_id] = Driver(
            id=driver_id,
            x_coordinate=x_coordinate,
            y_coordinate=y_coordinate
        )

    def _get_nearest_drivers_with_distance(self, x_coordinate: int, y_coordinate: int):
        nearest_drivers = []
        for driver in self.drivers.values():
            if driver.is_available is False:
                continue
            distance = calculate_distance(
                x1=x_coordinate,
                y1=y_coordinate,
                x2=driver.x_coordinate,
                y2=driver.y_coordinate,
            )
            if distance > MAX_DISTANCE_SEARCH:
                continue
            nearest_drivers.append((driver, distance))
        return nearest_drivers
    def get_nearest(self, x_coordinate: int, y_coordinate: int, limit: int = 5) -> List[Driver]:
        nearest_drivers = self._get_nearest_drivers_with_distance(
            x_coordinate=x_coordinate,
            y_coordinate=y_coordinate
        )
        nearest_drivers = sorted(nearest_drivers, key=lambda x: x[1])
        sorted_list = []
        for i in range(min(limit, len(nearest_drivers))):
            sorted_list.append(nearest_drivers[i][0])
        return sorted_list
