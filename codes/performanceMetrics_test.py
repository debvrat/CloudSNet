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

def writeToExcel(dataVec, filename):
	df = pd.DataFrame(np.array(dataVec))
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
	data = copy.copy(hdf5storage.loadmat(dataDir + file))
	delArr = []
	for x in data.keys():
		if ('CM' in x) and (('3' in x) or ('5' in x) or ('6' in x) or ('8' in x)):
			total+=data[x]
		# elif x.startswith('map') or x.startswith('train') or x.startswith('tile') or x=='imdb':
		# 	delArr.append(x)
	# for i in delArr:
	# 	del data[i]
	dataVec = metricCalc(total)
	os.chdir(outDir)
	writeToExcel(dataVec, str(file))
	#np.savetxt(str(file)+'.csv', metricVec, delimiter=',', fmt='%s')
	#hdf5storage.savemat(dataDir + file, data)


