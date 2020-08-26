import arcpy,os
from arcpy import env
from arcpy.sa import *

arcpy.env.workspace = r'D:\2'
arcpy.CheckOutExtension("spatial")

def tifToASCII(pathin,pathout):
    rasters = os.listdir(pathin)
    for raster in rasters:
        if raster[-4:] == ".tif":
            print raster
            in_raster = arcpy.Raster(raster)
            out_name = pathout + "/" + raster + ".txt"
            arcpy.RasterToASCII_conversion(in_raster,out_name)

    print "over!"
    return

if __name__ == "__main__":
    pathin = r'D:\2'
    pathout = r'D:\4_txt'
    tifToASCII(pathin,pathout)
