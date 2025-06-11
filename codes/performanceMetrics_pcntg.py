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

def writeToExcel(totalVec, testVec, trainVec, filename):
	df = pd.DataFrame({'Full Data': np.array(totalVec), 'Test Data': np.array(testVec), 'Train Data': np.array(trainVec)})
	writer = pd.ExcelWriter(filename+'.xlsx', engine='xlsxwriter')
	df.to_excel(writer)
	writer.save()

curDir = os.getcwd()
dataDir = curDir + '\\data\\' 
fileList = os.listdir(dataDir)
for file in fileList:
	print (str(file))
	data = copy.copy(hdf5storage.loadmat(dataDir + file))
	delArr = []
	for x in data.keys():
		if 'CM_map' in x:
			print (x)
			#print (data[x])
			#print (data[x][0])
			print ('clouds: ' + str((np.sum(data[x][0])/np.sum(data[x]))*100) + ' snow = ' + str((np.sum(data[x][1])/np.sum(data[x]))*100))




