from lib.kmlreader import write_kml
from src.commands.aim2gearth.process import *

def getJSONFromAim(nameInput: str):
    fileRead = open("data/input/aip/input.txt", "r")
    traceFolder = "data/input/kml/"

    arrayData = fileRead.readlines()
    arrayLength = len(arrayData)

    jsonFinal = line_type_identifier(traceFolder, arrayData, arrayLength)

    dataJson = json_to_sct_lines(jsonFinal)
    fileWrite = open("data/temp/test/outputSCT.txt", "w")

    for data in dataJson:
        fileWrite.write(data)
    with open("data/temp/json/fullBorder.json", "w") as jsonFile:
        json.dump(jsonFinal, jsonFile, indent=4)

    write_kml("data/temp/json/fullBorder", "out/kml/fullBorder"+nameInput, nameInput)