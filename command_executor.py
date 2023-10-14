from src.services.driver_manager import DriverManager
from src.services.fare_calculator import FareCalculator
from src.services.ride_manager import RideManager
from src.services.rider_manager import RiderManager


class CommandExecutor:

    driver_manager = DriverManager()
    rider_manager = RiderManager()
    ride_manager = RideManager(driver_manager=driver_manager, rider_manager=rider_manager)

    def add_driver(self, args):
        self.driver_manager.add(
            driver_id=args[1],
            x_coordinate=int(args[2]),
            y_coordinate=int(args[3])
        )

    def add_rider(self, args):
        self.rider_manager.add(
            rider_id=args[1],
            x_coordinate=int(args[2]),
            y_coordinate=int(args[3])
        )

    def start_ride(self, args):
        self.ride_manager.start_ride(
            ride_id=args[1],
            driver_number=int(args[2]),
            rider_id=args[3]
        )

    def match(self, args):
        self.ride_manager.match(rider_id=args[1])

    def stop_ride(self, args):
        self.ride_manager.stop_ride(
            ride_id=args[1],
            destination_x=int(args[2]),
            destination_y=int(args[3]),
            time_taken=int(args[4])
        )

    def bill(self, args):
        ride = self.ride_manager.get_ride(ride_id=args[1])
        if ride:
            if ride.is_completed is False:
                print("RIDE_NOT_COMPLETED")
                return
            FareCalculator().calculate(ride=ride)

    def execute(self, command_line):
        args = command_line.split()
        command = args[0]
        func = getattr(self, command.lower(), None)
        if func:
            func(args)

    def read_file(self, file_path):
        f = open(file_path, 'r')
        line = f.readline()
        while line:
            self.execute(command_line=line)
            line = f.readline()
