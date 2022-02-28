class Machine:
    def __init__(self, name, serialNumber, position, state):
        self.name = name
        self.serialNumber = serialNumber
        self.position = position
        self.state = state

    def toString(self):
        return f"Name: {self.name}, SerialNumber: {self.serialNumber}, position: {self.position.toString}, state: {self.State}"
