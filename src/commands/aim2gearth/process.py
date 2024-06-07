from src.commands.process import *
from lib.kmlreader import *
from lib.aipreader import *


def kml_radius_to_array(filename, sectorName, coords, radiusType):
    kmlCoordinate = read_kml_placemark(str(filename), sectorName)
    radiusCoordinate = coordinate_kml(radius_checker(kmlCoordinate, radiusType))
    coords = append_array(coords, radiusCoordinate)

    return coords

def kml_boundary_to_array(filename, sectorName, coords):
    kmlCoordinate = read_kml_placemark(str(filename), sectorName)
    boundaryCoordinate = coordinate_kml(kmlCoordinate)
    coords = append_array(coords, boundaryCoordinate)

    return coords

def line_type_identifier(traceFolder, arrayData, arrayLength):
    sectorName = ""
    iteration = 0
    jsonArea = 0
    coord = []
    jsonFinal = []

    while iteration < arrayLength:
        if(arrayData[iteration][:3].isnumeric() == False):
            if(arrayData[iteration][:6] == 'radius'):
                separator = arrayData[iteration][7:][:-1].split(" ")
                coord = kml_radius_to_array(traceFolder + separator[1] + " " + separator[2], separator[0] + " " + sectorName[9:], coord, separator[3])
                iteration += 1
                continue

            elif(arrayData[iteration][:8] == 'boundary'):
                separator = arrayData[iteration][9:][:-1]
                coord = kml_boundary_to_array(traceFolder+separator, sectorName[9:], coord)
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
    return jsonFinal

def json_to_sct_lines(datas):
    outputsData = []
    empty = ""
    for data in datas:
        sectorName = data["name"]

        for index in range(len(data["coordinate"])-1):
            if index == 0:
                coordinate1 = coordinate_dec_degminsec_converter(data["coordinate"][index])
                coordinate2 = coordinate_dec_degminsec_converter(data["coordinate"][index+1])

                outputsData.append(f"{sectorName:<40} {coordinate1[0]} {coordinate1[1]} {coordinate2[0]} {coordinate2[1]} COLOR_{sectorName[:3]}\n")
            elif index < len(data["coordinate"])-1:
                coordinate1 = coordinate_dec_degminsec_converter(data["coordinate"][index])
                coordinate2 = coordinate_dec_degminsec_converter(data["coordinate"][index+1])

                outputsData.append(f"{empty:<40} {coordinate1[0]} {coordinate1[1]} {coordinate2[0]} {coordinate2[1]} COLOR_{sectorName[:3]}\n")
            else:
                coordinate1 = coordinate_dec_degminsec_converter(data["coordinate"][index])
                coordinate2 = coordinate_dec_degminsec_converter(data["coordinate"][0])

                outputsData.append(f"{empty:<40} {coordinate1[0]} {coordinate1[1]} {coordinate2[0]} {coordinate2[1]} COLOR_{sectorName[:3]}\n")

        outputsData.append("\n")

    return outputsData