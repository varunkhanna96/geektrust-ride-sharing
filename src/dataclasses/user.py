import dataclasses


@dataclasses.dataclass
class User:
    id: str
    x_coordinate: int
    y_coordinate: int

    @staticmethod
    def user_type() -> str:
        return "User"


@dataclasses.dataclass
class Driver(User):
    is_available: bool = True

    def get_availability(self) -> bool:
        return self.is_available


@dataclasses.dataclass
class Rider(User):
    is_rider: bool = True

    @staticmethod
    def user_type() -> str:
        return "Rider"

    def get_is_rider(self) -> bool:
        return self.is_rider
