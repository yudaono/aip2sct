from lib.aipreader import *
from src.commands.process import *

def getBorderIndex(coord1, coord2):
    sameCoordinateIndexX = []
    sameCoordinateIndexY = []

    for x in range(len(coord1)):
        for y in range(len(coord2)):
            if(coord1[x] == coord2[y]):
                sameCoordinateIndexX.append(x)
                sameCoordinateIndexY.append(y)

    newIndexY = rearrange_array(sameCoordinateIndexY)
    newIndexX = rearrange_array(sameCoordinateIndexX)
    
    return newIndexX, newIndexY

def getNewSectorlineIndex(arr, oldArr):
    new_index = []
    for j, sub_arr in enumerate(arr):
        index = sub_arr[len(sub_arr)-1]
        new_index.append([])
        
        if len(arr)>1:
            if j == len(arr)-1:
                index_min = arr[0][0]
            else:
                index_min = arr[j+1][0]
        else:
            index_min = sub_arr[0]
        for i in range(len(oldArr)):
            new_index[j].append(index)
            index+=1
            if index == index_min+1:
                break
            if index == len(oldArr):
                index = 0
    return new_index

def getNewSectorline(arrIndex, oldData):
    new_index = getNewSectorlineIndex(arrIndex, oldData)
    new_sector = []
    for i, arr_index in enumerate(new_index):
        new_sector.append([])
        for j in arr_index:
            new_sector[i].append(oldData[j])

    return new_sector

def append_border_data(sectorsData, borderData, borderSectorIndex):
    for sectordex in range(0, len(sectorsData) - 1):
        for comparedIndex in range(sectordex+1, len(sectorsData)):
            coord1 = sectorsData[sectordex]["coordinate"]
            coord2 = sectorsData[comparedIndex]["coordinate"]

            coordInitial1 = isInitial(coord1)
            coordInitial2 = isInitial(coord2)

            nameBorder = str(sectorsData[sectordex]["name"] + "-" + sectorsData[comparedIndex]["name"][9:])
            borderIndex1, borderIndex2 = getBorderIndex(coordInitial1, coordInitial2)
            borderCoord = getBorderCoordinate(coordInitial1, borderIndex1)

            if(len(borderCoord)>1):
                nameBorder = str(sectorsData[sectordex]["name"] + "-" + sectorsData[comparedIndex]["name"][9:])

                borderSectorIndex[sectordex].append(borderIndex1)
                borderSectorIndex[comparedIndex].append(borderIndex2)

                borderData = append_json(nameBorder, borderCoord, borderData)
    return borderData, borderSectorIndex

def apppend_sectors_data(sectorsData, borderSectorIndex, newSectorsData):
    for i, data in enumerate(borderSectorIndex):
        newIndexData = combineArrays(data)
        oldData = sectorsData[i]["coordinate"]
        newSectorsLine = getNewSectorline(newIndexData, oldData)
        name = sectorsData[i]["name"]

        if len(newSectorsLine) > 1:
            index = 0
            for j in newSectorsLine:
                index += 1
                if len(j) < 2:
                    continue
                newSectorsData = append_json(name+"-"+str(index), j, newSectorsData)
        else:
            if len(newSectorsLine[0]) < 2:
                continue
            newSectorsData = append_json(name, newSectorsLine[0], newSectorsData)
    return newSectorsData

def line_bordering_process(sectorsData):
    borderData = []
    borderSectorIndex = []
    newSectorsData = []

    borderSectorIndex = empty_array(sectorsData, borderSectorIndex)

    borderData, borderSectorIndex = append_border_data(sectorsData, borderData, borderSectorIndex)
    newSectorsData = apppend_sectors_data(sectorsData, borderSectorIndex, newSectorsData)
    return borderData,newSectorsData

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