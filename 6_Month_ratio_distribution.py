import arcpy
from arcpy import env
from arcpy.sa import *

arcpy.env.workspace = r"E:\TRMM_nwd\TRMM_mon_nwd\2019"
arcpy.CheckOutExtension('spatial')

# 将文件按年份求比例
out_path = r"E:\\spatial_scaling\\TRMM_ratio_mon\\2019_ratio"
sum_f = r"E:\\spatial_scaling\\TRMM_year_nwd\\2019_BJ54_TRMM.tif"
rasters = arcpy.ListRasters('*','tif')
for raster in rasters:
#    if raster[0:4] == u"2001": #文件名为unicode格式需要声明
    print (raster)
    in_f = arcpy.Raster(raster)
    out_f = (in_f) / (sum_f)
    out_name = out_path + "//" + raster.split("_")[0] + "_ratio_mon.tif"
    print ("Processing file_name: " + raster)
    out_f.save(out_name)
    print ("Save_file name" + out_name)
print (arcpy.GetMessages())
print ("Over!")


