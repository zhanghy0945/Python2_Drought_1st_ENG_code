import arcpy,os
from arcpy import env
from arcpy.sa import *

arcpy.env.workspace = r'D:\TRMM_CN\TRMM_mon'
arcpy.env.scrathWorkspace = r'E:\trash'
arcpy.CheckOutExtension('spatial')
arcpy.overwriteOutput = 1


def accumulate_year_TRMM(pathin,pathout):
    data1 = []
    trmms = os.listdir(pathin)
    for trmm in trmms:
        if trmm[-4:] == ".tif" and trmm[0:4] == "2019":
            fn = trmm
            print fn
            in_raster = arcpy.Raster(fn)
            data1.append(in_raster)
    sum_trmm = CellStatistics([data1[:]],'SUM')
    out_name = pathout + "/" + fn[0:4] + '_TRMM_Y.tif'
    sum_trmm.save(out_name)

    print "over!"
    return
if __name__ == "__main__":
    pathin = r'D:\TRMM_CN\TRMM_mon'
    pathout = r'E:\TRMM_nwd\TRMM_year_nwd'
    accumulate_year_TRMM(pathin,pathout)
    
