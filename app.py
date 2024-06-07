import sys
sys.path.insert(0, 'E:/Vacc/Sectorfile/Software/SectorfileConverter')
from src.services.aim2gearth import getJSONFromAim
from src.services.sectorborderline import getSectorBorderLine

getJSONFromAim("test")
getSectorBorderLine("test")