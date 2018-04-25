import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import constants

def preprocessDesc(desc):
	desc = desc.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(desc)
	filtered_words = [w for w in tokens if not w in stopwords.words('english')]
	
	return " ".join(filtered_words)
	
def formatDescToArray(desc, features):
	
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
	return row

def loadDataSet(fileName):
	return np.genfromtxt(fileName, dtype='str', delimiter=',')	