import unittest
from unittest.mock import patch, Mock

from src.dataclasses.ride import Ride
from src.services.ride_manager import RideManager


class TestRideManager(unittest.TestCase):

    def test_get_ride_invalid(self):
        result = RideManager(
            driver_manager=Mock(),
            rider_manager=Mock()
        ).get_ride(ride_id="TEST_RIDE")

        assert result is None

    def test_get_ride_valid(self):
        ride = Ride(
            id="TEST_RIDE",
            driver_id="TEST_DRIVER",
            rider_id="TEST_RIDER",
            origin_x_coordinate=1,
            origin_y_coordinate=2
        )
        ride_manager = RideManager(
            driver_manager=Mock(),
            rider_manager=Mock()
        )
        with patch.object(ride_manager, "rides", new={"TEST_RIDE": ride}):
            response = ride_manager.get_ride(ride_id="TEST_RIDE")
            assert response == ride

    def test_stop_ride(self):
        ride = Ride(
            id="TEST_RIDE",
            driver_id="TEST_DRIVER",
            rider_id="TEST_RIDER",
            origin_x_coordinate=1,
            origin_y_coordinate=2
        )
        ride_manager = RideManager(
            driver_manager=Mock(),
            rider_manager=Mock()
        )
        with patch.object(ride_manager, "rides", new={"TEST_RIDE": ride}):
            response = ride_manager.stop_ride(ride_id="TEST_RIDE", destination_x=2, destination_y=3, time_taken=10)
            assert response is True
            assert ride.is_completed is True

    def test_stop_ride_completed(self):
        ride = Ride(
            id="TEST_RIDE",
            driver_id="TEST_DRIVER",
            rider_id="TEST_RIDER",
            origin_x_coordinate=1,
            origin_y_coordinate=2,
            is_completed=True
        )
        ride_manager = RideManager(
            driver_manager=Mock(),
            rider_manager=Mock()
        )
        with patch.object(ride_manager, "rides", new={"TEST_RIDE": ride}):
            response = ride_manager.stop_ride(ride_id="TEST_RIDE", destination_x=2, destination_y=3, time_taken=10)
            assert response is False
