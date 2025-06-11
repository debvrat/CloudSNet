import os
import copy
import scipy
import numpy as np
from scipy import stats
import hdf5storage
import pandas as pd


curDir = os.getcwd()
dataDir = curDir + '\\data\\' 
print (dataDir)
fileList = os.listdir(dataDir)
for file in fileList:
	print (str(file))
	total = np.zeros((4,4))
	data = copy.copy(hdf5storage.loadmat(dataDir + file))
	for x in data.keys():
		if 'CM' in x:
			total+=data[x]
	np.savetxt(str(file)+'.csv', total, delimiter=',', fmt='%s')

