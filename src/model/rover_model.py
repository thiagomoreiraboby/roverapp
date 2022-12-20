class RoverModel:
    def __init__(self, x:int, y:int, position:str):
        self.x = x
        self.y = y
        self.position = position

    def turn_right(self, coordinates: list):
        arrayindice = coordinates.index(self.position)
        if  arrayindice == (len(coordinates) -1):
            newindice = 0
        else:
            newindice = (arrayindice + 1)
        self.position = coordinates[newindice]
        

    def turn_left(self, coordinates: list):
        arrayindice = coordinates.index(self.position)
        if  arrayindice == 0:
            newindice = len(coordinates) -1
        else:
            newindice = arrayindice - 1
        self.position = coordinates[newindice]

    def move(self, coordinates_config, plateau):
        config = [x for x in coordinates_config if x["coor"] == self.position]
        xy = config[0].get("xy")
        value: int = config[0].get("value") 
        if xy == "x":
            newvaluex = self.x  + (value)
            if plateau.validate_positon_rover(newvaluex, self.y, self):
                self.x = newvaluex
        elif xy == "y":
            newvaluey = self.y + (value)
            if plateau.validate_positon_rover(self.x, newvaluey, self):
                self.y = newvaluey

    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.position}"
