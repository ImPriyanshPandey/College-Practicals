import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score , confusion_matrix
from sklearn.ensemble import BaggingClassifier , AdaBoostClassifier

#=======================Load The Dataset==========================#
data=pd.read_csv('customer_transaction_data.csv', encoding='latin-1')


#=============One-hot encode categorical columns=================#
data_encoded = pd.get_dummies(data)

#=======Split the data into predictors and target variables=======#
x = data_encoded.drop(columns=["Sales"])  # Predictors
y = data_encoded["Sales"]  # Target Variable

#===Create training and testing datasets (75% Train , 25% Test)===#
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.25,random_state=123)

#===================Descision Tree Classification=================# 
#==================Train the Descision Tree model=================#
model_tree=DecisionTreeClassifier()
model_tree.fit(x_train,y_train)

#=================Make Predictions on test set====================#
prediction_tree=model_tree.predict(x_test)

#===============Evaluate Descision Tree Performance===============#
accuracy_tree=accuracy_score(y_test,prediction_tree)

#==================Bagging with Descision Tree====================#
#=Create bagging ensemble with 3,3,7,9 Descision Tree Classifiers=#
Bagging_model=BaggingClassifier(base_estimator=DecisionTreeClassifier(),n_estimators=25)
Bagging_model.fit(x_train,y_train)
 
#==================Make Prediction On Test Set====================#
prediction_bagging=Bagging_model.predict(x_test)

#=================Evaluate Bagging Performance====================#
accuracy_bagging=accuracy_score(y_test,prediction_bagging)

#================AdaBoost with Descision Tree=====================#
#Create AdaBoost ensemble with 3,3,7,9 Descision Tree Classifiers #
AdaBoost_model=AdaBoostClassifier(base_estimator=DecisionTreeClassifier(),n_estimators=25)
AdaBoost_model.fit(x_train,y_train)
 
#==================Make Prediction On Test Set====================#
prediction_AdaBoost=AdaBoost_model.predict(x_test)

#=================Evaluate AdaBoost Performance====================#
accuracy_AdaBoost=accuracy_score(y_test,prediction_AdaBoost)

#===================Compare Performance=============================#
performance=pd.DataFrame({
    'Method': ['Descision Tree','Bagging','AdaBoost'] ,
    'Accuracy':[accuracy_tree,accuracy_bagging,accuracy_AdaBoost]   
})
print(performance)