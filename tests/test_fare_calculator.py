import unittest
from src.dataclasses.ride import Ride
from src.services.fare_calculator import FareCalculator


class TestFareCalculator(unittest.TestCase):

    def test_calculate_fare(self):
        ride = Ride(
            id="TEST_RIDE",
            driver_id="TEST_DRIVER",
            rider_id="TEST_RIDER",
            origin_x_coordinate=0,
            origin_y_coordinate=0,
            destination_x_coordinate=4,
            destination_y_coordinate=5,
            time_taken=32,
        )
        amount = FareCalculator().calculate(ride=ride)
        assert amount == 186.72
