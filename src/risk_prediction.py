import pandas as pd
import numpy as np

#Create user class
class patient:
    def __init__(self, patientid):
        self.id = patientid
        self.demographic_info = {}
        self.clinical_info = {}

#Create system class
class mhRiskPrediction:
    def __init__(self):
        self.model = model
        self.patients = []
    def add_patient(self, patient):
        self.patients.append(patient)
    def assess_patient(self, patient):
        #Prep for prediction
        patient_data = np.zeros(len(features))
        for i, feature in enumerate(features):
            if feature in patient.demographic_info:
                patient_data[i] = patient.demographic_info[feature]
            elif feature in patient.clinical_info:
                patient_data[i] = patient.clinical_info[feature]
            elif feature == 'patientid':
                patient_data[i] = patient.id
        #Make prediction
        prediction = self.model.predict([patient_data])[0]
        probability = self.model.predict_proba([patient_data])[0][1]
        
        return prediction, probability

    def get_result(self, patient, prediction, probability):
        report = f"Mental Health Risk Assessment for Patient: {patient.id}:\nRisk Status: {'High Risk' if prediction == 1 else 'Low Risk'}\nRisk Score: {probability: .2f}\n"
        report += "\nDemographic Info:\n"
        for key, value in patient.demographic_info.items():
            report += f"{key}: {value}\n"
        report += "\nClinical Info:\n"
        for key, value in patient.clinical_info.items():
            report += f"{key}: {value}\n"
        return report

##Usage Example
system = mhRiskPrediction()

#Add patient
patient1 = patient('000000001')
patient1.demographic_info = {'AGE':14, 'EDUC':5, 'ETHNIC':3, 'GENDER':1,'MARISTAT':4, 'EMPLOY':5, 
                             'DETNLF':1, 'RACE':6, 'VETERAN':2, 'LIVARAG':2, 'STATEFIP':18}
patient1.clinical_info = {'MH1':10, 'MH2':13, 'MH3':11, 'SUB':8, 'SAP':1, 'NUMMHS':3}
system.add_patient(patient1)

#Assess patient data
prediction, probability = system.assess_patient(patient1)

#View Result
result=system.get_result(patient1, prediction, probability)
print(result)
