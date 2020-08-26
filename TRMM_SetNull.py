 # -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:16:28 2020

@author: Administrator
"""

import arcpy,glob,os
from arcpy import env
from arcpy.sa import *

arcpy.env.workspace = r'D:\4_test'
arcpy.srcatchWorkspace = r'E:\trash'
arcpy.CheckOutExtension('spatial')
Nodata_value = "value = -3.40282346639e+38"

def Nodata(pathin,pathout):
    a = []
    datas = os.listdir(pathin)
    for ras in datas:
        if ras[-4:] == ".tif":
            print ras
            a.append(ras)
            in_raster = arcpy.Raster(ras)
            SetNull = arcpy.sa.SetNull(in_raster,in_raster,Nodata_value)
            outname = os.path.join(pathout, os.path.basename(ras)[0:6] + "_clip.tif")
            SetNull.save(outname)
    return ras
    print len(a)
    print "over"

if __name__ == "__main__":
    pathin = r'D:\4_test'
    pathout = r'F:\TRMM原数据\2019'
    Nodata(pathin,pathout)
