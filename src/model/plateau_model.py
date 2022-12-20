import logging

logger = logging.getLogger(__name__)
class PlateauModel:
    def __init__(self, size_x:int, size_y:int):
        self.size_x = size_x
        self.size_y = size_y

    def validate_positon_rover(self, new_value_x, new_value_y, rover) -> bool:
        if new_value_x > self.size_x or new_value_x < 0:
            logger.error(f"x: {new_value_x} coordinate of the rover:{rover} off the plateau: {self.size_x} X {self.size_y}")
            return False
        elif new_value_y > self.size_y or new_value_y < 0:
            logger.error(f"y: {new_value_y} coordinate of the rover:{rover} off the plateau: {self.size_x} X {self.size_y}")
            return False
        else: return True

    