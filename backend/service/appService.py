from helpers import configHelper
from models.Position import Position
import json
import requests

def getUrl():
    config = configHelper.read_config()
    url = config['Api']['apiUrl']
    return url

def GetMachine(serial):
    body = {"serialNumber": serial}
    return requests.get(f"{getUrl()}/machine/details?serialNumber={serial}")

def UpdateMachinePosition(machineDetail:Position):
    body = json.dump({f"machine:{machineDetail}"})   
    return requests.put(f"{getUrl()}/machine/details",body)