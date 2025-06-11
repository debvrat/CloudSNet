import os
import gdal
import numpy as np
from scipy import stats
	
b5 = gdal.Open('BAND5.tif')
# b4 = gdal.Open('BAND4.tif')
# b3 = gdal.Open('BAND3.tif')
b2 = gdal.Open('BAND2.tif')

green = np.array(b2.GetRasterBand(1).ReadAsArray())
swir = np.array(b5.GetRasterBand(1).ReadAsArray())
y, x = green.shape

ndsi = (green-swir)/(green+swir)
ndsi[ndsi >= 0.7] = 5
ndsi[ndsi < 0.7] = 1
ndsi[ndsi == 5] = 0

driver = gdal.GetDriverByName("GTiff")
outfile = driver.Create("ndsi.tif",x,y,1,gdal.GDT_UInt16)
outfile.SetProjection(b5.GetProjection())
outfile.SetGeoTransform(b5.GetGeoTransform())
outfile.GetRasterBand(1).WriteArray(ndsi)

# outfile.FlushCache()


# stackedArr = np.array([b2.GetRasterBand(1).ReadAsArray(),
# 		 b3.GetRasterBand(1).ReadAsArray(),
# 		 b4.GetRasterBand(1).ReadAsArray(),
# 		 b5.GetRasterBand(1).ReadAsArray()])
# y, x = stackedArr[0].shape
# driver = gdal.GetDriverByName("GTiff")
# # NRSC
# outfile = driver.Create("BAND.tif",x,y,4,gdal.GDT_UInt16)
# outfile.SetProjection(b4.GetProjection())
# outfile.SetGeoTransform(b4.GetGeoTransform())
# outfile.GetRasterBand(1).WriteArray(stackedArr[0])
# outfile.GetRasterBand(2).WriteArray(stackedArr[1])
# outfile.GetRasterBand(3).WriteArray(stackedArr[2])
# outfile.GetRasterBand(4).WriteArray(stackedArr[3])

# #CNN
# outfile = driver.Create("stacked.tif",x,y,3,gdal.GDT_UInt16)
# outfile.SetProjection(b4.GetProjection())
# outfile.SetGeoTransform(b4.GetGeoTransform())
# outfile.GetRasterBand(1).WriteArray(stackedArr[2])
# outfile.GetRasterBand(2).WriteArray(stackedArr[1])
# outfile.GetRasterBand(3).WriteArray(stackedArr[0])


outfile.FlushCache()

