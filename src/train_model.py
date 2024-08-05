from sklearn.ensemble import RandomForestClassifier

#Create Random Forest Classifier
model = RandomForestClassifier() 

#Fit Model
model.fit(X_train,y_train)

#Define predicted values
y_pred=pd.DataFrame(model.predict_proba(X_test))[1].values
