class Position:
    def __init__(self, serialNumber, x, y, theta):
        self.serialNumber = serialNumber
        self.x = x 
        self.y = y
        self.theta = theta
    def toString(self):
        return f"Coordinates: (x: {self.x}, y: {self.y}), theta: {self.theta}"