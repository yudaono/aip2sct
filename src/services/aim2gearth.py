import sys
sys.path.insert(0, 'E:/Vacc/Sectorfile/Software/SectorfileConverter')

from lib.kmlreader import *
from lib.aipreader import *
from src.commands.process import *

def getJSONFromAim(nameInput: str):
    fileRead = open("data/input/aip/input.txt", "r")
    traceFolder = "data/input/kml/"

    arrayData = fileRead.readlines()
    arrayLength = len(arrayData)

    sectorName = ""
    iteration = 0
    jsonArea = 0
    coord = []
    jsonFinal = []

    while iteration < arrayLength:
        if(arrayData[iteration][:3].isnumeric() == False):
            if(arrayData[iteration][:6] == 'radius'):
                separator = arrayData[iteration][7:][:-1].split(" ")
                coord = kml_radius_to_array(traceFolder + separator[1] + " " + separator[2], separator[0] + " " + sectorName, coord, separator[3])
                iteration += 1
                continue

            elif(arrayData[iteration][:8] == 'boundary'):
                separator = arrayData[iteration][9:][:-1]
                coord = kml_boundary_to_array(traceFolder+separator, sectorName, coord)
                iteration += 1
                continue

            elif(arrayData[iteration] == "\n"):
                if(arrayData[iteration+1] == "\n"):
                    iteration += 1
                    continue
                elif(arrayData[iteration+1][:3].isnumeric() == True):
                    iteration += 1
                    continue
                else:
                    jsonArea += 1
                    jsonFinal = append_json(sectorName, coord, jsonFinal)
                    coord = []

            else:
                sectorName = str(arrayData[iteration][:-1])

        else:
            Lat, Lon = degminsec_dec_converter(arrayData[iteration])
            coordinate_kml_append(coord, [Lon, Lat])
        iteration += 1

    append_json(sectorName, coord, jsonFinal)

    testJson = json_to_sct(jsonFinal)
    fileWrite = open("data/temp/test/output.txt", "w")
    for data in testJson:
        fileWrite.write(data)

    with open("data/temp/json/fullBorder.json", "w") as jsonFile:
        json.dump(jsonFinal, jsonFile, indent=4)

    write_kml("data/temp/json/fullBorder", "out/kml/fullBorder"+nameInput, nameInput)