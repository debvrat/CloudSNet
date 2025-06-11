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
print (dataDir)
outDir = curDir + '\\out_combined\\' 
fileList = os.listdir(dataDir)
for file in fileList:
	print (str(file))
	if 'L3' in str(file) or 'nrsc' in str(file):
		total = np.zeros((3,3))
		test = np.zeros((3,3))
		train = np.zeros((3,3))
	else:
		total = np.zeros((4,4))
		test = np.zeros((4,4))
		train = np.zeros((4,4))
	data = copy.copy(hdf5storage.loadmat(dataDir + file))
	delArr = []
	os.chdir(outDir)
	for x in data.keys():
		if 'CM' in x:
			total+=data[x]
			if ('3' in x) or ('5' in x) or ('6' in x) or ('8' in x):
				test+=data[x]
			if ('1' in x) or ('2' in x) or ('4' in x) or ('7' in x):
				train+=data[x]
	
	totalVec = metricCalc(total)
	testVec = metricCalc(test)
	trainVec = metricCalc(train)
	
	writeToExcel(totalVec, testVec, trainVec, str(file))
