import pandas as pd
import xgboost as XGBClassifier
from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from nltk.stem.snowball import SnowballStemmer



def parseOutText(s):
    words = ""
    if len(s) > 1:
        stemmer = SnowballStemmer("english")
        for i in s.split():
            words+=stemmer.stem(i)+' '
    return words.strip()

def preprocess():
      l=[]
      xl = pd.ExcelFile('C:\Users\A165885\Desktop\SNOWJan2018.xlsx')
      xl.sheet_names
      df = xl.parse("Request")

      for i in df['Description']:
          value=parseOutText(i)
          l.append(value)

      features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(l, df['Case Type Category'], test_size=0.1, random_state=42)
      ### text vectorization--go from strings to lists of numbers
      vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=1.0,
                                 stop_words='english',norm='l2', use_idf=True, smooth_idf=True)
      features_train_transformed = vectorizer.fit_transform(features_train)
      features_test_transformed  = vectorizer.transform(features_test)

      selector = SelectPercentile(f_classif, percentile=1)
      selector.fit(features_train_transformed, labels_train)
      features_train_transformed = selector.transform(features_train_transformed).toarray()
      features_test_transformed  = selector.transform(features_test_transformed).toarray()
      #print "no. of Sara training emails:", len(labels_train)-sum(labels_train)
      
      return features_train_transformed, features_test_transformed, labels_train, labels_test

# =============================================================================
# 
                
     
features_train, features_test, labels_train, labels_test = preprocess()
#clf = GaussianNB()
#clf.fit(features_train, labels_train)
#pred=clf.predict(features_test)
#accuracy= accuracy_score(labels_test, pred)
#print accuracy
# 
# =============================================================================
model = XGBClassifier()
model.fit(features_train, labels_train)
# make predictions for test data
y_pred = model.predict(features_test)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(labels_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
