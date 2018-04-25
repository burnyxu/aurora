import numpy as np
import constants
import math
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus
import pdb
from sklearn.tree import _tree
import pickle
import util

	
	
# calculate shanon entropy of the given data set
def calcEntropy(dataSet):
	
	# get all categories
	rowCount = len(dataSet)
	#cat = set()
	categoryAndCount = {}
	for row in dataSet:
		cat = row[-1]
		if cat in categoryAndCount:
			categoryAndCount[cat] += 1
		else:
			categoryAndCount[cat] = 1
	
	entropy = 0.0
	#calculate entropy
	for cat in categoryAndCount:
	
		p = categoryAndCount[cat]/rowCount
		
		entropy += - p * (math.log(p, 2))
		
		

	print("entropy: ", entropy)
	

def sklearnDt(trainingSet, features, testingSet):
	
	x = trainingSet[:, :-1]
	y = trainingSet[:, -1]
	
	dataFrame = pd.DataFrame(x, columns=features)
	
	#print(x)
	#print(y)
	
	dtree=DecisionTreeClassifier()
	dtree.fit(dataFrame,y)
	
	
	pkl = open(constants.CONST_DTREE_FILE_NAME, "wb+")
	pickle.dump(dtree,pkl)
	
	#test
	testX = testingSet[:,:-1]
	testY = testingSet[:, -1]
	score = dtree.score(testX, testY)
	print("dt score is : ", score)
	
	dot_file = 'tree.dot'
	pdf_file = 'tree.pdf'
	
	#pdb.set_trace()
	
	with open(dot_file, 'w') as f:
		dot_data = export_graphviz(dtree, out_file=f,  filled=True, rounded=True,special_characters=True)
		
		#graph = pydotplus.graph_from_dot_data(dot_file) 
		#graph.write_pdf(pdf_file) 			
		

def sklearnSVC(trainingSet, testingSet):
	x = trainingSet[:, :-1]
	y = trainingSet[:, -1]
	
	svc = SVC()
	svc.fit(x, y)

	#test
	testX = testingSet[:,:-1]
	testY = testingSet[:, -1]
	score = svc.score(testX, testY)
	print("svc score is : ", score)

def sklearnKNN(trainingSet, testingSet):
	x = trainingSet[:, :-1]
	y = trainingSet[:, -1]
	
	kNN = KNeighborsClassifier()
	kNN.fit(x, y)

	#test
	testX = testingSet[:,:-1]
	testY = testingSet[:, -1]
	score = kNN.score(testX, testY)
	print("KNN score is : ", score)	

		
	
	
if __name__ == "__main__":
	
	
	np.set_printoptions(threshold=np.nan)
	
	trainingSet = util.loadDataSet(constants.CONST_TRAINING_FILENAME)
	
	testingSet = util.loadDataSet(constants.CONST_TESTING_FILENAME)
	
	features = util.loadDataSet(constants.CONST_FEATURE_FILENAME)
	
	#print(features)
	
	sklearnDt(trainingSet, features, testingSet)
	
	sklearnSVC(trainingSet, testingSet)
	
	sklearnKNN(trainingSet, testingSet)
	
	#calcEntropy(trainingSet)
	
	
#dot -Tpdf tree.dot -o tree.pdf	