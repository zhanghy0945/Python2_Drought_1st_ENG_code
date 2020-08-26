import arcpy,os
from arcpy import env
from arcpy.sa import *

arcpy.env.workspace = r'D:\First_ENG_Article\TRMM_1'
arcpy.CheckOutExtension("spatial")

def hourTomonth(pathin,pathout):
    datas = os.listdir(pathin)
    for data in datas:
        if data[-4:] == ".tif":
            if data[4:6] == "01" or data[4:6]== "03" or data[4:6]== "05" or data[4:6]== "07" or data[4:6]== "08" or data[4:6]== "10" or data[4:6]== "12":
                print data
                in_raster = arcpy.Raster(data)
                out_raster = in_raster * float(31.0 * 24.0)
                out_name = pathout + '/' + data[0:8] + ".tif"
                out_raster.save(out_name)
            elif data[4:6] == "04" or data[4:6] == "06" or data[4:6] == "09" or data[4:6] == "11":
                print data
                in_rster = arcpy.Raster(data)
                out_raster = in_raster * float(30.0 * 24.0)
                out_name = pathout + '/' + data[0:8] + ".tif"
                out_raster.save(out_name)
            elif data[4:6] == "02":
                print data
                in_raster = arcpy.Raster(data)
                if int(data[0:4]) / 400 != 0:
                    print "平年2月28天："
                    out_raster = in_raster * float(28.0 * 24.0)
                    out_name = pathout + '/' + data[0:8] + ".tif"
                    out_raster.save(out_name)
                elif int(data[0:4]) / 400 == 0:
                    print "闰年2月29天："
                    out_raster = in_raster * float(29.0 * 24.0)
                    out_name = pathout + '/' + data[0:8] + ".tif"
                    out_raster.save(out_name)
                    
if __name__ == "__main__":
    pathin = r'D:\First_ENG_Article\TRMM_1'
    pathout = r'D:\First_ENG_Article\TRMM_2'
    hourTomonth(pathin,pathout)
