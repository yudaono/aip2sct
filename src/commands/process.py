from lib.kmlreader import *
from lib.aipreader import *

def append_array(coordinates, newCoordinates):
    for inside in newCoordinates:
        coordinates.append(inside)

    return coordinates

def coordinate_kml(coords):
    coordinate = []
    for iter in coords:
        coordinate_kml_append(coordinate, iter)

    return coordinate

def coordinate_kml_append(coordinate, data):
    coordinate.append(str(data[0])+","+str(data[1])+",0"+"\n")
    
    return coordinate

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

def json_to_sct(datas):
    outputsData = []
    empty = ""
    for data in datas:
        sectorName = data["name"]
        #Print sectorName

        for index in range(len(data["coordinate"])-1):
            if index == 0:
                coordinate1 = coordinate_dec_degminsec_converter(data["coordinate"][index])
                coordinate2 = coordinate_dec_degminsec_converter(data["coordinate"][index+1])

                outputsData.append(f"{sectorName:<40} {coordinate1[0]} {coordinate1[1]} {coordinate2[0]} {coordinate2[1]} test\n")
            elif index < len(data["coordinate"])-1:
                coordinate1 = coordinate_dec_degminsec_converter(data["coordinate"][index])
                coordinate2 = coordinate_dec_degminsec_converter(data["coordinate"][index+1])

                outputsData.append(f"{empty:<40} {coordinate1[0]} {coordinate1[1]} {coordinate2[0]} {coordinate2[1]} test\n")
            else:
                coordinate1 = coordinate_dec_degminsec_converter(data["coordinate"][index])
                coordinate2 = coordinate_dec_degminsec_converter(data["coordinate"][0])

                outputsData.append(f"{empty:<40} {coordinate1[0]} {coordinate1[1]} {coordinate2[0]} {coordinate2[1]} test\n")

    return outputsData

def coordinate_dec_degminsec_converter(data):
    coordinate = data.split(",")

    idLat, idLon = dec_degminsec_identifier(coordinate)
    latDeg, latMnt, latSec = dec_degminsec_converter(coordinate[1])
    lonDeg, lonMnt, lonSec = dec_degminsec_converter(coordinate[0])

    coordinates = [f"{idLat}{int(latDeg):03}.{int(latMnt):03}.{latSec:06.3f}", f"{idLon}{int(lonDeg):03}.{int(lonMnt):03}.{lonSec:06.3f}"]

    return coordinates