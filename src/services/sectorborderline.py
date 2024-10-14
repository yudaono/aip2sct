import json
from src.commands.sectorborderline.process import *
from lib.kmlreader import write_kml

def getSectorBorderLine(nameInput: str):
    with open('data/temp/json/fullBorderEarth.json', 'r') as file:
        sectorsData = json.load(file)
    
    borderData, newSectorsData = line_bordering_process(sectorsData)
    fileWrite = open("data/temp/test/outputSCTTest.txt", "w")

    dataOuterJson = json_to_sct_lines(newSectorsData)
    fileWriteOuter = open("data/temp/test/outputSCT_checkerOuter.txt", "w")
    dataBorderJson = json_to_sct_lines(borderData)
    fileWriteBorder = open("data/temp/test/outputSCT_checkerBorder.txt", "w")

    for data in dataOuterJson:
        fileWriteOuter.write(data)
        fileWrite.write(data)
    for data in dataBorderJson:
        fileWriteBorder.write(data)
        fileWrite.write(data)
    with open("data/temp/json/dataBorder.json", "w") as jsonFile:
        json.dump(borderData, jsonFile, indent=4)
    with open("data/temp/json/dataOuter.json", "w") as jsonFile:
        json.dump(newSectorsData, jsonFile, indent=4)

    write_kml("data/temp/json/dataBorder", "out/kml/"+"test"+"Border", nameInput+"_BORDER")
    write_kml("data/temp/json/dataOuter", "out/kml/"+"test"+"Outer", nameInput+"_OUTER")