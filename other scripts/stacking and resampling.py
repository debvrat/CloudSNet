import os
import gdal
import numpy as np
mainDir = os.getcwd()
subDir = os.listdir(os.getcwd())

for x in subDir:
        if '.py' in x:
                subDir.remove(x)
        else:
                chDir = mainDir + '\\' + x + '\\'
				uniqueScenes = os.listdir(chDir)
				
                stackBands(chDir)
                print (x[:11] + ' complete')
                os.chdir(mainDir)

				
def stackBands (directory):
        os.chdir(directory)
        b4 = gdal.Open(directory + 'BAND4.tif')
        b3 = gdal.Open(directory + 'BAND3.tif')
        b2 = gdal.Open(directory + 'BAND2.tif')
        stackedArr = np.array([b4.GetRasterBand(1).ReadAsArray(),
                 b3.GetRasterBand(1).ReadAsArray(),
                 b2.GetRasterBand(1).ReadAsArray()])
        y, x = stackedArr[0].shape
        driver = gdal.GetDriverByName("GTiff")
        outfile = driver.Create("stacked.tif",x,y,3,gdal.GDT_UInt16)
        outfile.SetProjection(b4.GetProjection())
        outfile.SetGeoTransform(b4.GetGeoTransform())
        outfile.GetRasterBand(1).WriteArray(stackedArr[0])
        outfile.GetRasterBand(2).WriteArray(stackedArr[1])
        outfile.GetRasterBand(3).WriteArray(stackedArr[2])
        outfile.FlushCache()