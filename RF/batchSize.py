import gdal
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
import numpy as np
import pickle
import copy
from sklearn.metrics import confusion_matrix
import pandas as pd
import myFuncs
import createData
import functools


break_flag=0
trainingData = createData.trainingData
trainingLabels = createData.trainingLabels
testData = createData.testData
testLabels = createData.testLabels
tempData = copy.deepcopy(trainingData)
tempLabels = copy.deepcopy(trainingLabels)

batch_size = 5000
batch_size_opt=0
labelSize = len(tempLabels)
print('labelSize = ' + str(labelSize))
while (batch_size != 0):
	print('batch_size = ' + str(batch_size))
	for i in range(labelSize//batch_size + 1):
		print("		batch No. = " + str(i))
		if(len(np.unique(tempLabels[i*batch_size:((i+1)*batch_size - 1)])) !=4 ):
			batch_size += 5000
			break
		elif (i == (labelSize//batch_size)):
			print('---- optimum batch_size = ' + str(batch_size))
			batch_size_opt = batch_size
			batch_size = 0


batch_size = batch_size_opt
for i in range(len(tempData)// batch_size + 1):
	print("-- batch " + str(i) + " - " + str(i*batch_size) + " to " + str(((i+1)*batch_size - 1)) + " - unique classes = " + str(np.unique(tempLabels[i*batch_size:((i+1)*batch_size - 1)])))