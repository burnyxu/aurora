import constants
import util
import pickle
from sklearn.tree import DecisionTreeClassifier

def loadDTreeFromFile():
	with open(constants.CONST_DTREE_FILE_NAME, 'rb') as pklFile:
		dtree = pickle.load(pklFile)
		
	return dtree

def formatData(str):
	#load features from file
	features = util.loadDataSet(constants.CONST_FEATURE_FILENAME)
	
	return util.formatDescToArray(util.preprocessDesc(str), features)

def predict(str):
	return ""

if __name__ == "__main__":

	dtree = loadDTreeFromFile()
	
	desc = "Hello,Please, could you update the following customer CDB 1453216057 with the PARMA 1194991 BR Mgane."
	
	descArray = formattedDesc = formatData(desc)
	
	data = []
	
	data.append(descArray)
	
	cat = dtree.predict(data)
	
	print(cat)
	
	