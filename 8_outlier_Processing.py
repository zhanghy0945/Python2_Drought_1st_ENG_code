# -*- coding: utf-8 -*-

import arcpy
from arcpy import env
from arcpy.sa import *


arcpy.env.workspace = r"E:\\spatial_scaling\\TRMM_1km_year" #存放数据的路径
arcpy.scratchWorkspace = r'E:\trash'
arcpy.CheckOutExtension("Spatial")
pathout = r"E:\\spatial_scaling\\TRMM_1km_year_Smooth"

where_clause = "value < 0"
in_data = arcpy.ListRasters("*","tif")

for data in in_data:
    print (data)
    in_raster = arcpy.Raster(data)
    print ("Processing the file: " + data) 
    out_raster = Con(in_raster,FocalStatistics(in_raster,NbrRectangle(90,90,"CELL"),"MEAN",""),in_raster,where_clause)
    out_path = pathout + "//" + data[0:4] + "_HRs_TRMM.tif"
    out_raster.save(out_path)
    print ("Save as: " + out_path)
print ("Over!")



