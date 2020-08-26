import arcpy
from arcpy import env
from arcpy.sa import *

arcpy.env.workspace = r""
arcpy.CheckOutExtension("spatial")

rasters = arcpy.ListRasters("*","tif")
for  raster in rasters:
    print (raster,type(raster))
    in_f = arcpy.Raster(raster)
    