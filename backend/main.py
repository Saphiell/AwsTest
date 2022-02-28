from enums.machineStateEnum import MachineState
from models.Machine import Machine
from models.Position import Position
from service.appService import GetMachine, UpdateMachinePosition
import time
import json

device1 =  Machine("Test1","Test11", Position('Test11',0,0,0),MachineState.Paused)
device2 = Machine("Test2","Test22", Position('Test22',0,0,0),MachineState.Active)

def selectDevice():
    selectedDevice = int(input("Select machine between number 1 or 2: "))

    serialNumber = "";
    if selectedDevice == 1:
        serialNumber = device1.serialNumber
    elif selectedDevice == 2:
        serialNumber = device2.serialNumber
    else:
        print("Wrong number, please try again")
        serialNumber = selectDevice()
    
    return serialNumber;

def updatePosition(machine, goingDown):
    #assume we have a rectangle 100x100
    if machine.position.x < 100 and goingDown:
        machine.position.x += 1
        machine.position.theta = 0
    elif machine.position.x == 100 and machine.position.y <= 100 and goingDown:
        machine.position.y += 1
        machine.position.theta = 90
        goingDown = False
    elif machine.position.x > 0 and (not goingDown):
        machine.position.x -= 1
        machine.position.theta = 0
    elif machine.position.x == 100 and machine.position.y == 100:
        #reset machine back to original position
        machine.position.y = 0  
        machine.position.x = 0
        machine.position.theta = 0
        goingDown = True
    elif machine.position.x == 0 and not goingDown:
        machine.position.y += 1
        goingDown = True

    UpdateMachinePosition(machine.position)
    return goingDown

def main():
    goingDown = True;
    state = MachineState.Errored
    while True:
        response = GetMachine(selectDevice())
        if response is not None and response.status_code == 200:
            machine = json.load(response.text)
            if machine.state == MachineState.Active:
                if machine.state != state:
                    print("Machine in active state");
                goingDown = updatePosition(machine, goingDown)   
            elif machine.state == MachineState.Errored:
                if machine.state != state:
                    print("Machine in paused state");
            else:
                if machine.state != state:
                    print("Machine in paused state");
                    
            time.sleep(10)
            state = machine.state 
        

main()