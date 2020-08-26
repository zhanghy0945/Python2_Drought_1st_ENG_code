#Read the ASCII file and conversion projection
# write by zhy NWNU
import os

def ASCIIwrite(pathin):
    file_path = pathin
    fs = os.listdir(pathin)
    for f in fs:
        if f[-4:] == ".txt":
            print f
            file_path = pathin
            with open(file_path,'r',encoding = 'utf-8') as f_1:
                print f_1.readlines()
            
            


if __name__ == "__main__":
    pathin = r'D:\4_txt'
    ASCIIwrite(pathin)
    
                
