import os
import gdal
import numpy as np
	
b5 = gdal.Open('BAND5.tif')
b4 = gdal.Open('BAND4.tif')
b3 = gdal.Open('BAND3.tif')
b2 = gdal.Open('BAND2.tif')
stackedArr = np.array([b5.GetRasterBand(1).ReadAsArray(),
		 b4.GetRasterBand(1).ReadAsArray(),
		 b3.GetRasterBand(1).ReadAsArray(),
		 b2.GetRasterBand(1).ReadAsArray()])
y, x = stackedArr[0].shape
driver = gdal.GetDriverByName("GTiff")
outfile = driver.Create("BAND.tif",x,y,3,gdal.GDT_UInt16)
outfile.SetProjection(b4.GetProjection())
outfile.SetGeoTransform(b4.GetGeoTransform())
outfile.GetRasterBand(1).WriteArray(stackedArr[0])
outfile.GetRasterBand(2).WriteArray(stackedArr[1])
outfile.GetRasterBand(3).WriteArray(stackedArr[2])
#outfile.GetRasterBand(4).WriteArray(stackedArr[3])
outfile.FlushCache()

