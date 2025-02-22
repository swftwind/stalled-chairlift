from ChairState import ChairState  # Import ChairState Enum

class Chair:
    def __init__(self, chair_number: int, chair_state: ChairState, x: float, y: float, z: float, is_first_chair: bool = False):
        self.is_first_chair = is_first_chair
        self.chair_number = chair_number
        self.chair_state = chair_state
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return (f"Chair({self.chair_number}, {self.chair_state.name}, "
                f"x={self.x}, y={self.y}, z={self.z}, First={self.is_first_chair})")
