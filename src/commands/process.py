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

def isInitial(coord):
    if coord[0] == coord[len(coord) - 1]:
        coord = coord[:-1]

    return coord

def rearrange_array(arr):
    index = 0
    if arr:
        arr.sort()
        for num in range(len(arr)-1):
            if arr[num] == arr[num+1]-1:
                index+=1
            else:
                newIndex =[]
                index+=1
                for num in range(len(arr)):
                    newIndex.append(arr[index])
                    index+=1
                    if index == len(arr):
                        index = 0

                return newIndex

    return arr

def combineArrays(arr):
    combined = []
    
    for sub_arr in arr:
        merged = False
        for i, combined_sub_arr in enumerate(combined):
            if sub_arr[0] == combined_sub_arr[-1]:
                combined[i].extend(sub_arr[1:])
                merged = True
                break
            elif sub_arr[-1] == combined_sub_arr[0]:
                combined[i] = sub_arr[:-1] + combined_sub_arr
                merged = True
                break
                
        if not merged:
            combined.append(sub_arr)

    return combined

def getBorderCoordinate(coord, borderIndex):
    newCoord = []
    if borderIndex:
        for index in borderIndex:
            newCoord.append(coord[index])

    return newCoord

def empty_array(dataForLength, dataAppend):
    for i in range(len(dataForLength)):
        dataAppend.append([])
    
    return dataAppend
