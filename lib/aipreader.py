def radius_checker(coords: any, radiusType: str):
    if(radiusType == "anticlockwise"):
        coords = coords[::-1]

    return coords

def append_json(sectorName, coordinate, finalJSON):
    jsonFormat = {"name" : sectorName, "coordinate" : coordinate}
    finalJSON.append(jsonFormat)

    return finalJSON

def degminsec_dec_converter(data):
    ii = str(data)
    Lat =  format(float(int(ii[0:2])+int(ii[2:4])/60 + int(ii[4:6])/3600), '.8f')
    Lon =  format(float(int(ii[8:11])+int(ii[11:13])/60 + int(ii[13:15])/3600), '.8f')
    if(ii[6] == "S"):
        Lat = "-" + Lat
    if(ii[14] == "W"):
        Lon = "-" + Lon

    return Lat, Lon

def dec_degminsec_converter(data):
    mnt,sec = divmod(abs(float(data))*3600,60)
    deg,mnt = divmod(mnt,60)

    return deg, mnt, sec

def dec_degminsec_identifier(coordinate):
    identLat = "N"
    identLon = "E"
    if (float(coordinate[1])) < 0:
        identLat = "S"
    if (float(coordinate[0])) < 0:
        identLon = "W"
    
    return identLat, identLon