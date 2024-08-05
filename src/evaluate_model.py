#Cross Validation
from sklearn.model_selection import cross_val_predict

y_pred = cross_val_predict(model, X_test, y_test, cv=5) 

from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
# Metrics
print("F1 score:", f1_score(y_test, y_pred, average='binary'))
print("ROC AUC:", roc_auc_score(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("Confusion Matrix:", confusion_matrix(y_test, y_pred))
