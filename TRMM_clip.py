
import arcpy,os,glob
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension('spatial')

arcpy.env.workspace = r'D:\First_ENG_Article\TRMM_2' 

def extractByMask(pathin,pathout):
    datas = os.listdir(pathin)
    in_Mask = r'E:\NWdesert\NW_desert_new.shp'
    for i in datas:
        if  i[-4:] == ".tif":#and i[0:4] == "2018" and len(i) <= 10:
            print i
            ras_i = arcpy.Raster(i)
            out_raster = ExtractByMask(ras_i,in_Mask)
            outname = os.path.join(pathout, os.path.basename(i)[0:6] + '_TRMM_nwd.tif')
            out_raster.save(outname)
    print i
    print "over!"
    return 
if __name__ == "__main__":
    pathin = r'D:\First_ENG_Article\TRMM_2'
    pathout = r'D:\First_ENG_Article\TRMM_3'
    extractByMask(pathin,pathout)  
#    pathout = r""
