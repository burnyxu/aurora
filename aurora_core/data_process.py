from __future__ import division
from nltk import FreqDist

import pandas as pds
import os
import nltk
import pdb
import sys
import math
import numpy
import constants
import util


def readDataFromExcel():
	
	combinedData = pds.DataFrame()
	
	for file in os.listdir(constants.CONST_DATA_FILE_FOLDER):
		if (file.endswith(".xlsx") and (not file.startswith("~$"))):
			filePath = os.path.join(constants.CONST_DATA_FILE_FOLDER, file)
			print("start reading : " + filePath)
			#read excel file
			xl = pds.ExcelFile(filePath)
			df = xl.parse(constants.CONST_EXCEL_SHEET_REQUEST)
			
			combinedData = pds.concat([combinedData, df])
	
	
	
	for index, row in combinedData.iterrows():			
		cat = row[constants.CONST_EXCEL_COLUMN_TYPE]
		if(cat == 'Others'):
			print("aa")
	
	
	print("data set size is : " , len(combinedData.index))
	
	
	
	return combinedData

def getAllCategories(combinedData):
	
	allCategories = set()
	
	for cat in combinedData[constants.CONST_EXCEL_COLUMN_TYPE]:
		allCategories.add(cat)		
	
	
	
	return allCategories
	
def getFeatures(combinedData, x):
	
	allCategories = getAllCategories(combinedData)
	
	catAndDesc = {}
	
	for cat in allCategories:
		catAndDesc[cat] = []
	
	for index, row in combinedData.iterrows():
		cat = row[constants.CONST_EXCEL_COLUMN_TYPE]		
		desc = util.preprocessDesc(str(row[constants.CONST_EXCEL_COLUMN_DESCRIPTION]))
		tokens = nltk.word_tokenize(desc)
		catAndDesc[cat].extend(tokens)
		
	features = set()
	
	
	for cat in catAndDesc:
		fdist = FreqDist(catAndDesc[cat])
		mostCommon = fdist.most_common(x)
		
		for keyword in mostCommon:
			if keyword[0] != '\xc2':
				features.add(keyword[0])
		
		#print(cat)
		#print(mostCommon)
		
	print("features size is : ", len(features))
	
	return features
	
def constructTrainingTestingData(features, combinedData):
	
	print(features)
	
	allDataCount = len(combinedData.index)
	
	trainingDataCount = int(allDataCount * constants.CONST_TRAINING_DATA_PERCENTIGE / 100)
	
	testingDataCount = allDataCount - trainingDataCount
	
	formattedData = []
	
	
	
	print("training data size: ", trainingDataCount, " testing data size: ", testingDataCount)
	
	print("started formatting data.")
	
	for index, row in combinedData.iterrows():
		cat = row[constants.CONST_EXCEL_COLUMN_TYPE]
		desc = util.preprocessDesc(str(row[constants.CONST_EXCEL_COLUMN_DESCRIPTION]))
		tokens = nltk.word_tokenize(desc)
		row = []
		for feature in features:
			hit = False
			for token in tokens:				
				if token == feature:
					row.append(constants.CONST_TAG_YES)
					hit = True
					break
			if not hit:			
				row.append(constants.CONST_TAG_NO)
		row.append(cat)
		formattedData.append(row)
	
	#print(formattedData)	
	
	print("formating data done.")
	
	print("start saving data.")
	
	trainingSet = formattedData[:trainingDataCount]
	testingSet = formattedData[trainingDataCount:]
	
	numpy.savetxt(constants.CONST_TRAINING_FILENAME, trainingSet, fmt='%5s',delimiter=',')
	numpy.savetxt(constants.CONST_TESTING_FILENAME, testingSet, fmt='%5s',delimiter=',')
	numpy.savetxt(constants.CONST_FEATURE_FILENAME, [list(features)], fmt='%5s', delimiter=',')
	
	print("end saving data.")
	
	
	
#def buildDecisionTree():

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
		#pdb.set_trace()
		entropy += - p * (math.log(p, 2))

	print("entropy: ", entropy)
	
		
if __name__ == "__main__":
		
	
	#reload(sys)
	
	#sys.setdefaultencoding('utf-8')
	
	
	combinedData = readDataFromExcel()
	
	features = getFeatures(combinedData,constants.CONST_KEYWORDS_COUNT_EACH_CATE)
	
	constructTrainingTestingData(features, combinedData)
		

	