import json
from lib.kmlreader import read_kml_sector_area

def getJSONfromGearth(nameInput: str):
    traceFolder = "data/input/kml/"
    coordinates = read_kml_sector_area(traceFolder + nameInput )
    with open("data/temp/json/fullBorderEarth.json", "w") as jsonFile:
        json.dump(coordinates, jsonFile, indent=4)
        
