import arcpy,os
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension('spatial')
arcpy.env.workspace = r'D:\TRMM3B43_2019'

f = []
hdfs = []
datas = arcpy.ListRasters("*","hdf")
print datas
for data in datas:
    strname = str(data)
    f.append(strname)
    print strname,type(strname)

    hdf = arcpy.Raster(data)
    print hdf,type(hdf)
    hdfs.append(hdf)
    outname = strname.split(".")[2][0:8] + ".tif"

    outfile = arcpy.ExtractSubDataset_management(hdf,outname,"0")

    

    



