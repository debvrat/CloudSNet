import os
import copy
import scipy
import numpy as np
from scipy import stats
import hdf5storage
import pandas as pd
import xlsxwriter

def metricCalc(confMat):
	pa_c = confMat[0,0] / np.sum(confMat[:,0])
	ua_c = confMat[0,0] / np.sum(confMat[0,:]) 
	pa_sn = confMat[1,1] / np.sum(confMat[:,1])
	ua_sn = confMat[1,1] / np.sum(confMat[1,:]) 
	f_c = stats.hmean([pa_c, ua_c])
	f_sn = stats.hmean([pa_sn, ua_sn])
	f_2cls = np.mean([f_c, f_sn])
	oa = np.trace(confMat)/np.sum(confMat)
	return pa_c*100, ua_c*100, pa_sn*100, ua_sn*100, f_c*100, f_sn*100, f_2cls*100, oa*100

def writeToExcel(totalVec, testVec, filename):
	df = pd.DataFrame({'Full Data': np.array(totalVec), 'Test Data': np.array(testVec)})
	writer = pd.ExcelWriter(filename+'.xlsx', engine='xlsxwriter')
	df.to_excel(writer)
	writer.save()

curDir = os.getcwd()
dataDir = curDir + '\\data\\' 
print (dataDir)
outDir = curDir + '\\out_test\\' 
fileList = os.listdir(dataDir)
for file in fileList:
	print (str(file))
	total = np.zeros((4,4))
	test = np.zeros((4,4))
	oaAllTiles = np.zeros(8)
	data = copy.copy(hdf5storage.loadmat(dataDir + file))
	for x in data.keys():
		if 'CM' in x:
			total+=data[x]
			if ('3' in x) or ('5' in x) or ('6' in x) or ('8' in x):
				test+=data[x]
	oaAllTiles = np.trace(total)/np.sum(total)
	oaTestTiles = np.trace(test)/np.sum(test)
	print (str(file) + ' oaAllTiles: ' +  oaAllTiles + ' oaTestTiles: ' + oaTestTiles)



