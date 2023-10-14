import dataclasses
from typing import Optional
from src.helper import calculate_distance


@dataclasses.dataclass
class Ride:
    id: str
    rider_id: str
    driver_id: str
    origin_x_coordinate: int
    origin_y_coordinate: int
    destination_x_coordinate: Optional[int] = None
    destination_y_coordinate: Optional[int] = None
    time_taken: Optional[int] = None
    is_completed: bool = False

    def get_total_distance(self):
        return calculate_distance(
            self.origin_x_coordinate,
            self.origin_y_coordinate,
            self.destination_x_coordinate,
            self.destination_y_coordinate,
        )
