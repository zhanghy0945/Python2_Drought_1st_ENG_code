import arcpy,os
from arcpy import env
from arcpy.sa import *

arcpy.env.workspace = r'D:\1'
arcpy.CheckOutExtension("spatial")

datas = arcpy.ListRasters("*","tif")
outpath = r'D:\2'
for data in datas:
    print data,type(data)
    name = str(data)
#    print name,type(name)
    in_raster = arcpy.Raster(data)
    pivot_point = "-0.5 -1439.5"
    out_name = outpath + "/" + name
    out_raster = arcpy.Rotate_management(in_raster, out_name, "-90",pivot_point,"BILINEAR")



