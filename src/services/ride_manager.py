from typing import Optional

from src.dataclasses.ride import Ride
from .driver_manager import DriverManager
from .rider_manager import RiderManager


class RideManager:

    def __init__(self, driver_manager: DriverManager, rider_manager: RiderManager):
        self._driver_manager = driver_manager
        self._rider_manager = rider_manager
        self.rides = {}
        self.matched_drivers = {}

    def match(self, rider_id: str) -> None:
        rider = self._rider_manager.get_rider(rider_id)
        drivers = self._driver_manager.get_nearest(
            x_coordinate=rider.x_coordinate,
            y_coordinate=rider.y_coordinate,
            limit=5
        )
        if not drivers:
            print("NO_DRIVERS_AVAILABLE")
            return
        self.matched_drivers[rider_id] = drivers
        matched_drivers = " ".join(map(lambda x: x.id, drivers))
        print(f"DRIVERS_MATCHED {matched_drivers}")

    def _is_valid_ride(self, ride_id: str, driver_number: int, rider_id: str):
        if (
            ride_id in self.rides or
            len(self.matched_drivers.get(rider_id, [])) < driver_number or
            self.matched_drivers[rider_id][driver_number-1].is_available is False
        ):
            print("INVALID_RIDE")
            return False

    def start_ride(self, ride_id: str, driver_number: int, rider_id: str) -> bool:
        if self._is_valid_ride(ride_id, driver_number=driver_number, rider_id=rider_id) is False:
            return False
        driver = self.matched_drivers[rider_id][driver_number - 1]
        rider = self._rider_manager.get_rider(rider_id=rider_id)
        driver.is_available = False
        ride = Ride(
            id=ride_id,
            rider_id=rider_id,
            driver_id=driver.id,
            origin_x_coordinate=rider.x_coordinate,
            origin_y_coordinate=rider.y_coordinate,
        )
        self.rides[ride_id] = ride
        print(f"RIDE_STARTED {ride_id}")
        return True

    def stop_ride(self, ride_id: str, destination_x: int, destination_y: int, time_taken: int) -> bool:
        if ride_id not in self.rides or self.rides[ride_id].is_completed:
            print("INVALID_RIDE")
            return False
        ride = self.rides[ride_id]
        ride.is_completed = True
        ride.destination_x_coordinate = destination_x
        ride.destination_y_coordinate = destination_y
        ride.time_taken = time_taken
        print(f"RIDE_STOPPED {ride_id}")
        return True

    def get_ride(self, ride_id) -> Optional[Ride]:
        if ride_id not in self.rides:
            print("INVALID_RIDE")
            return
        return self.rides[ride_id]
