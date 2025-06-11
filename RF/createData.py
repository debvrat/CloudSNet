import gdal
import numpy as np
import pandas as pd
import myFuncs

trainingLabels = []
trainingData = []
#isTrain renamed to lblIdx

#training Data ------------------------------------
tile1 = r"train/TR_9OCT_1.tif"
tile2 = r"train/TR_9OCT_2.TIF"
tile3 = r"train/13may_1.tif"
tile4 = r"train/13may_4.tif"

rasterDS1 = gdal.Open(tile1, gdal.GA_ReadOnly)
rasterDS2 = gdal.Open(tile2, gdal.GA_ReadOnly)
rasterDS3 = gdal.Open(tile3, gdal.GA_ReadOnly)
rasterDS4 = gdal.Open(tile4, gdal.GA_ReadOnly)


roiRaster1 = r"train/roi/TR_9OCT_1_ROI.tif"
lblRaster1 = (gdal.Open(roiRaster1, gdal.GA_ReadOnly)).ReadAsArray()
roiRaster2 = r"train/roi/TR_9OCT_2_ROI.tif"
lblRaster2 = (gdal.Open(roiRaster2, gdal.GA_ReadOnly)).ReadAsArray()
roiRaster3 = r"train/roi/13may_1_roi.tif"
lblRaster3 = (gdal.Open(roiRaster3, gdal.GA_ReadOnly)).ReadAsArray()
roiRaster4 = r"train/roi/13may_4_roi.tif"
lblRaster4 = (gdal.Open(roiRaster4, gdal.GA_ReadOnly)).ReadAsArray()

lblIdx = np.nonzero(lblRaster1)
lblRaster1 = lblRaster1[lblIdx]
bandsData1 = myFuncs.bandDatatoNumpy(rasterDS1)
bandsData1 = bandsData1[lblIdx]

lblIdx = np.nonzero(lblRaster2)
trainingLabels = np.append(lblRaster1, lblRaster2[lblIdx])
bandsData2 = myFuncs.bandDatatoNumpy(rasterDS2)
trainingData = np.concatenate((bandsData1, bandsData2[lblIdx]))

lblIdx = np.nonzero(lblRaster3)
trainingLabels = np.append(trainingLabels, lblRaster3[lblIdx])
bandsData3 = myFuncs.bandDatatoNumpy(rasterDS3)
trainingData = np.concatenate((trainingData, bandsData3[lblIdx]))

lblIdx = np.nonzero(lblRaster4)
trainingLabels = np.append(trainingLabels, lblRaster4[lblIdx])
bandsData4 = myFuncs.bandDatatoNumpy(rasterDS4)
trainingData = np.concatenate((trainingData, bandsData4[lblIdx]))
print('trainingData shape = ' + str(trainingData.shape))

#test Data ------------------------------------

tile5 = r"test/TS_9OCT_1.tif"
tile6 = r"test/13may_2.tif"
tile7 = r"test/13may_3.tif"
tile8 = r"test/13may_6.tif"

rasterDS5 = gdal.Open(tile5, gdal.GA_ReadOnly)
rasterDS6 = gdal.Open(tile6, gdal.GA_ReadOnly)
rasterDS7 = gdal.Open(tile7, gdal.GA_ReadOnly)
rasterDS8 = gdal.Open(tile8, gdal.GA_ReadOnly)


roiRaster5 = r"test/roi/TS_9OCT_1_ROI.tif"
lblRaster5 = (gdal.Open(roiRaster5, gdal.GA_ReadOnly)).ReadAsArray()
roiRaster6 = r"test/roi/13may_2_roi.tif"
lblRaster6 = (gdal.Open(roiRaster6, gdal.GA_ReadOnly)).ReadAsArray()
roiRaster7 = r"test/roi/13may_3_roi.tif"
lblRaster7 = (gdal.Open(roiRaster7, gdal.GA_ReadOnly)).ReadAsArray()
roiRaster8 = r"test/roi/13may_6_roi.tif"
lblRaster8 = (gdal.Open(roiRaster8, gdal.GA_ReadOnly)).ReadAsArray()


lblIdx = np.nonzero(lblRaster5)
lblRaster5 = lblRaster5[lblIdx]
bandsData5 = myFuncs.bandDatatoNumpy(rasterDS5)
bandsData5 = bandsData5[lblIdx]

lblIdx = np.nonzero(lblRaster6)
testLabels = np.append(lblRaster5, lblRaster6[lblIdx])
bandsData6 = myFuncs.bandDatatoNumpy(rasterDS6)
testData = np.concatenate((bandsData5, bandsData6[lblIdx]))

lblIdx = np.nonzero(lblRaster7)
testLabels = np.append(testLabels, lblRaster7[lblIdx])
bandsData7 = myFuncs.bandDatatoNumpy(rasterDS7)
testData = np.concatenate((testData, bandsData7[lblIdx]))

lblIdx = np.nonzero(lblRaster8)
testLabels = np.append(testLabels, lblRaster8[lblIdx])
bandsData8 = myFuncs.bandDatatoNumpy(rasterDS8)
testData = np.concatenate((testData, bandsData8[lblIdx]))

print('testData shape = ' + str(testData.shape))