#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import re
import random as rd
import readline

# Reading of the training data
attributes = ['ID',
'radius_mean',
'texture_mean',
'perimeter_mean',
'area_mean',
'smoothness_mean',
'compactness_mean',
'concavity_mean',
'concave_mean',
'symmetry_mean',
'fractal_mean',
'class{M|B}']

trainData = pd.read_csv('cancerTrainingData.csv', skiprows=12, header=None) ## Skipping first 12 lines since they are header lines
trainData.columns = attributes
trainData.index = trainData["ID"]


# Subsetting of the both malignant and benign rows and means of the attributes
# Getting first ten colums, since first ten columns are the features

malignTrain = trainData[trainData["class{M|B}"] == 'M'] 
benignTrain = trainData[trainData["class{M|B}"] == 'B']
malignAtt = malignTrain.iloc[:,0:10] 
malignAtt = malignAtt.mean(axis = 0)
benignAtt = benignTrain.iloc[:, 0:10]
benignAtt = benignAtt.mean(axis = 0)

# Construction of the data frame with the average of malignant and benign attributes, and midpoint classifier

midpoint = pd.DataFrame({'Malignant': malignAtt, 'Benign': benignAtt})

midpoint["Classifier"] = midpoint.mean(axis = 1)



##Function that classifies according to training data

def Classifier(row, majorityThreshold = 5, thresholds = midpoint["Classifier"]):
    
    """
    This function evaluates all the features for a given patient and compares
    them with the classifier midpoint values To make a decision for each feature.
    Finally, depending on the number of malignant features and majority threshold,
    the function predicts a diagnosis.
    """
    
    TorF = []
    for e, feature in enumerate(row):
        if feature > thresholds[e]:
            TorF.append("Malignant")
        else:
            TorF.append("Benign")
    if TorF.count("Malignant") >= majorityThreshold:
        return ("Malignant", TorF)
    else:
        return ("Benign", TorF)
    
    

## Calculating the accuracy with changing the majority threshold

testData = pd.read_csv('cancerTestingData.csv', skiprows=12, header=None)
testData.columns = attributes
testData.index = testData["ID"]

testdf = testData.iloc[:,0:9]

for majThreshold in range(5,8):
    predict = []
    perAcc = []
    for i, row in testdf.iterrows():
        tmpclassif = Classifier(row, majorityThreshold=majThreshold)[0]
        pattern = r"^."
        foundPat = re.findall(pattern, tmpclassif)[0]
        predict.append(foundPat)
    testData["Predicted Class"] = predict
    testData["truePrediction"] = testData["class{M|B}"] == testData["Predicted Class"]
    perAcc = testData['truePrediction'].mean(axis = 0) * 100
    truePred = testData['truePrediction'].sum()
    print("For threshold %i, percent acuracy is: %.2f, %i total correct assignment." %(majThreshold, perAcc, truePred) )

testData["Predicted Class"] = predict
testData["truePrediction"] = testData["class{M|B}"] == testData["Predicted Class"] 

rownamesMidpoint = midpoint.index.values
rownamesMidpoint = [re.sub('_mean', '', x) for x in rownamesMidpoint]


#------------------------------------------

#Front end preparation

midpoint['Key'] = rownamesMidpoint

cols = ["Key", "Malignant", "Classifier", "Benign"]

### Conversion of midpoint data frame to string for the interface

midpoint_p = midpoint[cols]
midpoint_p = midpoint_p.reset_index(drop=True)
new_row = pd.DataFrame(dict(zip(cols, ['', 'Average', 'Midpoint', 'Average'])), index = [0])
midpoint_p = pd.concat([new_row, midpoint_p]).reset_index(drop = True)
midpoint_s = midpoint_p.to_string(col_space = 15, float_format = lambda x: "{:.3f}".format(x))
midpoint_s_list = midpoint_s.split("\n")
midpoint_s_list = [re.sub("^.{2}", "", x) for x in midpoint_s_list]
midpoint_s = "\n".join(midpoint_s_list)

def patientQuery(patient, patientData = testData, classifierInfo = midpoint):
    key = classifierInfo['Key']
    patientValue = patientData.loc[patient][0:10]
    classifierCol = classifierInfo["Classifier"] 
    finalDecision, classCol = Classifier(patientValue.get_values().reshape(-1,))
    results = pd.DataFrame({"Key": key, 
                            "Patient": patientValue, 
                            "Classifier": classifierCol,
                            "Class": classCol})
    cols = ['Key', 'Patient', 'Classifier', 'Class']
    new_row = pd.DataFrame(dict(zip(cols, ['', 'Value', 'Cutoff', ''])), index = [0])
    results = pd.concat([new_row, results]).reset_index(drop = True)
    results_s = results.to_string(col_space = 15, float_format = lambda x: "{:.3f}".format(x))
    results_s_list = results_s.split("\n")
    results_s_list = [re.sub("^.{2}", "", x) for x in results_s_list]
    results_s = "\n".join(results_s_list)
    return (finalDecision, results_s)

print("Classifier, benign and malignant stats")

print("="*80)

print(midpoint_s)

print("Reading in test data...")
      
testData = pd.read_csv('cancerTestingData.csv', skiprows=12, header=None)
testData.columns = attributes
testData.index=testData["ID"]
      
print("Done reading test data.")
predict = []
for i, row in testdf.iterrows():
    tmpclassif = Classifier(row, majorityThreshold=6)[0]
    pattern = r"^."
    foundPat = re.findall(pattern, tmpclassif)[0]
    predict.append(foundPat)
    
testData["Predicted Class"] = predict

testData["truePrediction"] = testData["class{M|B}"] == testData["Predicted Class"] 

print("Done classifying.")

correctAssign = testData['truePrediction'].sum()

totalRecord = len(testData['truePrediction'])

print("The classifier correctly predicted the class (malignant/benign) of %i records out of %i records." % (correctAssign, totalRecord))

percentAccuracy = float(testData['truePrediction'].mean(axis = 0)) * 100

print("The classifier achieved an accuracy of %.2f percent" % percentAccuracy)

## Program for the user to input the ID of the patient

while 1:
    patientNo = input("Type an ID to check a patient ('quit' to stop): ")
    
    if patientNo != "quit":
        try:
            intPatientNo = int(patientNo)
            print("Checking ID:%s's clasification" % patientNo)
            overallDiagnosis, classification = patientQuery(intPatientNo)
            print(classification)
            print("Overall Diagnosis for patient %s: %s " % (patientNo, overallDiagnosis))
            continue
        except KeyError:
            print("The patient ID that you have typed is not found, please try again or type quit to exit")
            continue
        except ValueError:
            print("Patient ID should be a number, please try again")
            continue
    else:
        print("Program finished.")
        break

        
## Simulation for generating new patient data of 250 records        
        
maxVal= testData.index.values.max()
minVal = testData.index.values.min()

### Generation of new patient IDs with random sampling of the IDs of the test data

newPatientID = []
for i in range(250):
    newID = rd.randrange(minVal, maxVal + 1)    
    if newID not in newPatientID: 
        newPatientID.append(newID)
        continue
    while newID in newPatientID:
        newID = rd.randrange(minVal, maxVal + 1)
    newPatientID.append(newID)    
    
    
malignant = rd.sample(newPatientID, 125)
benign= list(set(newPatientID).difference(set(malignant)))
simulation = pd.DataFrame(dict(zip(midpoint["Key"], [None for i in range(10)])), index = newPatientID)



midpointC = midpoint.copy()
listIndex = [re.sub(r"_mean", "", x) for x in midpointC.index.values]
midpointC.index = listIndex

## This loop chooses number of features randomly to be malignant and given the number chooses the features randomly based on the number, then assigns the numbers to be above the threshold 

for ID in malignant:
    nMalignft = rd.randint(5,10)
    malignft = rd.sample(list(simulation.columns), nMalignft)
    benignft = list(set(list(simulation.columns)).difference(set(malignft)))
    for ft in malignft:
        tmp = midpointC.loc[ft]
        minV = tmp[2]
        maxV = tmp[0]
        ftVal = rd.uniform(minV, maxV)
        simulation.loc[ID, ft] = ftVal
    for ft in benignft:
        tmp = midpointC.loc[ft]
        minV = tmp[1]
        maxV = tmp[2]
        ftVal = rd.uniform(minV, maxV)
        simulation.loc[ID, ft] = ftVal        
        

## This loop chooses number of features randomly to be benign and given the number chooses the features randomly based on the number, then assigns the numbers to be below the threshold 

for ID in benign:
    nMalignft = rd.randint(0,5)
    malignft = rd.sample(list(simulation.columns), nMalignft)
    benignft = list(set(list(simulation.columns)).difference(set(malignft)))
    for ft in malignft:
        tmp = midpointC.loc[ft]
        minV = tmp[2]
        maxV = tmp[0]
        ftVal = rd.uniform(minV, maxV)
        simulation.loc[ID, ft] = ftVal
    for ft in benignft:
        tmp = midpointC.loc[ft]
        minV = tmp[1]
        maxV = tmp[2]
        ftVal = rd.uniform(minV, maxV)
        simulation.loc[ID, ft] = ftVal
        
## Writing simulated data to csv file
simulation["class{M|B}"] = None
for ID in benign:
	simulation.loc[ID,"class{M|B}"] = "B"

for ID in malignant:
	simulation.loc[ID,"class{M|B}"] = "M"


simulation.to_csv("cancerSimulatedData.csv", index=False, encoding="utf-8")
