#!/usr/bin/python3


class RoverManager():
    def __init__(self):
        self.rovers = []

    def instruct(self, data):
        lines = data.split("\n")
        self.plateau_dimensions = [int(n) for n in lines[0].split(" ")]
        
        instructions = lines[1:]
        for i in range(0, len(instructions), 2):
            rover_positions = [[r.x, r.y] for r in self.rovers]
            rover = Rover(self.plateau_dimensions, rover_positions)
            rover.instruct(instructions[i], instructions[i+1])
            self.rovers.append(rover)

        results = []
        for rover in self.rovers:
            results.append("{} {} {}".format(rover.x, rover.y, rover.compass_point))
        return '\n'.join(results)
    

class Rover():
    compass_points = ['N', 'E', 'S', 'W']

    def __init__(self, plateau_dimensions, rover_positions):
        self.x = 0
        self.y = 0
        self.compass_point = 'N'
        self.plateau_dimensions = plateau_dimensions
        self.rover_positions = rover_positions

    def spin_left(self):
        idx = self.compass_points.index(self.compass_point)
        if idx == 0:
            idx = len(self.compass_points) - 1
        else:
            idx -= 1
        self.compass_point = self.compass_points[idx]

    def spin_right(self):
        idx = self.compass_points.index(self.compass_point)
        if idx == len(self.compass_points) - 1:
            idx = 0
        else:
            idx += 1
        self.compass_point = self.compass_points[idx]
    
    def is_position_free(self, x, y):
        return [x, y] not in self.rover_positions

    def is_position_on_plateau(self, x, y):
        return x >= 0 and x <= self.plateau_dimensions[0] \
            and y >= 0 and y <= self.plateau_dimensions[1]

    def move(self):
        if self.compass_point == 'N':
            if self.is_position_free(self.x, self.y + 1) \
                and self.is_position_on_plateau(self.x, self.y + 1):
                self.y += 1
                
        elif self.compass_point == 'E':
            if self.is_position_free(self.x + 1, self.y) \
                and self.is_position_on_plateau(self.x + 1, self.y):
                self.x += 1

        elif self.compass_point == 'S':
            if self.is_position_free(self.x, self.y - 1) \
                and self.is_position_on_plateau(self.x, self.y - 1):
                self.y -= 1

        elif self.compass_point == 'W':
            if self.is_position_free(self.x - 1, self.y) \
                and self.is_position_on_plateau(self.x - 1, self.y):
                self.x -= 1

    def instruct(self, start, movement):
        x, y, self.compass_point = start.split(" ")
        self.x = int(x)
        self.y = int(y)
        for item in movement:
            if item == "L":
                self.spin_left()
            elif item == "R":
                self.spin_right()
            elif item == "M":
                self.move()
