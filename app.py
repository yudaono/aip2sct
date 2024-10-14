import sys
sys.path.insert(0, 'E:/Vacc/Sectorfile/Software/SectorfileConverter')
# from src.services.aim2gearth import getJSONFromAim
from src.services.sectorborderline import getSectorBorderLine
from src.services.gearth2json import getJSONfromGearth

# getJSONFromAim("test")
getJSONfromGearth("UJUNG UTA")
getSectorBorderLine("UJUNG UTA")