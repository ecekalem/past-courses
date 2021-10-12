import numpy as np

def parseLine(n):
    
    """Parses the PDB atom records"""
    
    
    atomDict = {
        'serialNumber': int(n[6:11]),
        'atomName': n[12:16].strip(),
        'resName': n[17:20].strip(),
        'chainid': n[21].strip(),
        'resNo': int(n[22:26]),
		'insertions': n[26],
        'x': float(n[30:38]),
        'y': float(n[38:46]),
        'z': float(n[46:54]),
        'occupancy': float(n[54:60]),
        'tempFact': float(n[60:66]),
        'segmentId': n[72:76],
        'elementSymbol': n[76:78],
        'charge': n[78:80]
        
    }
    return atomDict


pdbList = []


# parsing the pdb file
for line in open('/home/ece/Downloads/6o31.pdb'):
    if line.startswith('ATOM'):
        xd = parseLine(line)
        if xd['atomName'] in ['N', 'CA', 'C'] and xd['chainid'] == 'A':
            pdbList.append(xd)
            
def bondLength(a, b):
    
    """Calculates the euclidian distance between atoms"""
    
    bondlength = ((a[0] - b[0])**2 + (a[1] - b[1])**2  + (a[2] - b[2])**2)**0.5
    return bondlength


###Q5 RMSD
import math

def rmsd(list1, list2):
"""Calculates the RMSD values between two models"""    
    zaa = []
    for j in range(len(list1)):
        coor1 = [list1[j][i] for i in ('x', 'y', 'z')]
        coor2 = [list2[j][i] for i in ('x', 'y', 'z')]
        zaa.append((bondLength(coor1, coor2))**2)
        
    return math.sqrt(sum(zaa)/len(zaa))


##Q3
resNo = [i['resNo'] for i in pdbList]

atomMatrix = np.zeros((np.max(resNo), np.max(resNo)))
tempFacs = np.zeros(np.max(resNo))

### Filling the contact matrix, and retrieving temperature factors 
for atom1 in pdbList:
    if atom1['atomName'] == 'CA':
        resNo1 = atom1['resNo']
        bFac = atom1['tempFact']
        tempFacs[resNo1-1] = bFac
        for atom2 in pdbList:
            if atom2['atomName'] == 'CA':
                resNo2 = atom2['resNo']
                coordinates1 = [atom1[i] for i in ('x', 'y', 'z')]
                coordinates2 = [atom2[i] for i in ('x', 'y', 'z')]
                temp = bondLength(coordinates1, coordinates2)
                if temp < 7:
                    atomMatrix[resNo1-1][resNo2-1] = temp
                    
np.savetxt('atomMatrix.csv', atomMatrix, delimiter = ',')
np.savetxt('tempFactor.csv', tempFacs, delimiter = ',')
    

###Parsing the NMR models
modelDict = dict()
for line in open('/home/ece/Downloads/6u3r.pdb'):
    if line.startswith('MODEL'):
        modelKey = line.split()[1]
        modelDict[modelKey] = []
    elif line.startswith('ATOM'):    
        xd = parseLine(line)
        if xd['atomName'] in ['CA'] and xd['chainid'] == 'A':
            modelDict[modelKey].append(xd)    
    elif line.startswith('ENDMDL'):
        continue
        
###RMSD
### Calculation of the RMSD values for each model vs model 1
rmsdList = []
for model in modelDict:
    print(model)
    rmsdList.append(rmsd(modelDict[model], modelDict['1']))

rmsdList = np.array(rmsdList)
modelNumbers = np.array(list(range(2,11)))
np.savetxt('rmsdList.csv', rmsdList, delimiter= ',')

correlation = np.corrcoef(rmsdList, modelNumbers)
print(correlation)



### Q4 Centroid

xCoor = [i['x'] for i in pdbList]
yCoor = [i['y'] for i in pdbList]
zCoor = [i['z'] for i in pdbList]

##4a
centroid = [np.mean(i) for i in [xCoor, yCoor, zCoor]]

pdbListShift = []
### Shifting the centroid to origin
for i in range(len(pdbList)):
    tmp = pdbList[i].copy()
    for j,k in enumerate(('x','y','z')):
        tmp[k] = tmp[k] - centroid[j]
    pdbListShift.append(tmp)
    
xcorSh = [i['x'] for i in pdbListShift]
ycorSh = [i['y'] for i in pdbListShift]
zcorSh = [i['z'] for i in pdbListShift]

### Checking the condition for each dimension
zeromu = [sum(i) for i in (xcorSh, ycorSh, zcorSh)]
print(zeromu)

### Writing shifted coordinates to the file
fields =  ['serialNumber',
        'atomName',
        'resName',
        'chainid',
        'resNo',
		'insertions',
        'x',
        'y',
        'z',
        'occupancy',
        'tempFact',
        'segmentId',
        'elementSymbol',
        'charge']

fl = open("6o31_shifted.pdb", "w")

for line in pdbListShift:
	line_s = [str(line[i]) for i in fields]
	line_s = ["ATOM"] + line_s
	line_s = "\t".join(line_s)
	fl.write(line_s +"\n")

fl.close()


# charNums = [5, 4, 1, 3, 1, 4, 1, 8, 8, 8, 6, 6, 4, 2, 2]
# 
# whitesp =  [2, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0 ,0, 6, 0, 0] ##leading ws for each field
# 
# for line in pdbListShift:
# 	for field,charNum,ws in (fields, charNums,whitesp):
# 		thisField = line[field]
# 		if type(thisField) != 'str':
# 			l = len(str(thisField)) 
# 			if l < charNum:
# 				thisField = ' ' * (l-charNum) + str(thisField)
# 			else:
# 				s = '{.2f}'.format(thisField)
# 				l = len(s)
# 				thisField = ' ' * (l-
# 
#     
