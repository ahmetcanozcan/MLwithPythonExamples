#!/usr/bin/python
import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
"""
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
"""
################################################################################


### your code here!  name your classifier object clf if you want the 
from sklearn.naive_bayes import GaussianNB 
clf = GaussianNB()
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
acc =accuracy_score(pred,labels_test)
print "Gaussian  acc",acc



from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.metrics import accuracy_score

clf = RFC()
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
acc =accuracy_score(pred,labels_test)
print "defaule acc",acc

print "For different n_estimators:"
print "----------------------------"
max_acc , max_est = 0 , 0
for i in [1,2,4,8,10,16,25,50,32,64,100,200]:#For estimators in n_estimators
	clf = RFC(n_estimators=i,random_state=42)
	clf.fit(features_train,labels_train)
	pred = clf.predict(features_test)
	acc =accuracy_score(pred,labels_test)
	if(acc> max_acc):
		max_est = i
		max_acc = acc
	
	print "Accuracy of the forest for acc",i,acc

print "For different max_depth:"
print "----------------------------"
print max_est
for i in [None,1,32,64]:#For max_depth in max_depths
	clf = RFC(max_depth=i,n_estimators=max_est,random_state=0)
	clf.fit(features_train,labels_train)
	pred = clf.predict(features_test)

	print "Accuracy of the forest for max depth",i,accuracy_score(pred,labels_test)


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
