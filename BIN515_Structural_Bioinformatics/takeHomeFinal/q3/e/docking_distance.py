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


receptorList = []
dasatinibList = []

# parsing the pdb file

for line in open('/home/ece/Desktop/structuralBioinformatics/FinalTakeHome/q3/PDB_files/Dasatinib_dock.pdb'):
    #print(line)
    if line.startswith('ATOM'):
        xd = parseLine(line)
        ##print(xd)
        dasatinibList.append(xd)
        
imatinibList = []        
for line in open('/home/ece/Desktop/structuralBioinformatics/FinalTakeHome/q3/PDB_files/imatinib_docked.pdb'):
    #print(line)
    if line.startswith('ATOM'):
        xd = parseLine(line)
        ##print(xd)
        imatinibList.append(xd)
        
        
lesinuradList = []        
for line in open('/home/ece/Desktop/structuralBioinformatics/FinalTakeHome/q3/PDB_files/lesinurad_docked.pdb'):
    #print(line)
    if line.startswith('ATOM'):
        xd = parseLine(line)
        ##print(xd)
        lesinuradList.append(xd)


nilotinibList = []        
for line in open('/home/ece/Desktop/structuralBioinformatics/FinalTakeHome/q3/PDB_files/nilotinib_docked.pdb'):
    #print(line)
    if line.startswith('ATOM'):
        xd = parseLine(line)
        ##print(xd)
        nilotinibList.append(xd)

def dist(a, b):
    
    """Calculates the euclidian distance between atoms"""
    
    distance = ((a[0] - b[0])**2 + (a[1] - b[1])**2  + (a[2] - b[2])**2)**0.5
    return distance

######
receptorRes = []
dasatinibRes = []
tmp = []
for atom1 in receptorList:
    for atom2 in dasatinibList:
        atom1_coord = [atom1[i] for i in ("x", "y", "z")]
        atom2_coord = [atom2[i] for i in ("x", "y", "z")]
        d = dist(atom1_coord, atom2_coord)
        tmp.append(d)
        if d <= 6:
            receptorRes.append(atom1['resNo'])
            dasatinibRes.append(atom2['resNo'])
        else:
            continue
            



receptorRes_l = set(receptorRes)
receptorRes_l = [str(x) for x in receptorRes_l]
" ".join(receptorRes_l)

######
receptorRes1 = []
imatinibRes = []

for atom1 in receptorList:
    for atom2 in imatinibList:
        atom1_coord = [atom1[i] for i in ("x", "y", "z")]
        atom2_coord = [atom2[i] for i in ("x", "y", "z")]
        d = dist(atom1_coord, atom2_coord)
        tmp.append(d)
        if d <= 6:
            receptorRes1.append(atom1['resNo'])
            imatinibRes.append(atom2['resNo'])
        else:
            continue
            
            
receptorRes1_l = set(receptorRes1)
receptorRes1_l = [str(x) for x in receptorRes1_l]
" ".join(receptorRes_l)
receptorRes_l = set(receptorRes)
receptorRes_l = [str(x) for x in receptorRes_l]
" ".join(receptorRes1_l)
#####


receptorRes2 = []
lesinuradRes = []

for atom1 in receptorList:
    for atom2 in lesinuradList:
        atom1_coord = [atom1[i] for i in ("x", "y", "z")]
        atom2_coord = [atom2[i] for i in ("x", "y", "z")]
        d = dist(atom1_coord, atom2_coord)
        tmp.append(d)
        if d <= 6:
            receptorRes2.append(atom1['resNo'])
            lesinuradRes.append(atom2['resNo'])
        else:
            continue
            
            
receptorRes2_l = set(receptorRes2)
receptorRes2_l = [str(x) for x in receptorRes2_l]
" ".join(receptorRes2_l)

#####

receptorRes3= []
nilotinibRes = []

for atom1 in receptorList:
    for atom2 in nilotinibList:
        atom1_coord = [atom1[i] for i in ("x", "y", "z")]
        atom2_coord = [atom2[i] for i in ("x", "y", "z")]
        d = dist(atom1_coord, atom2_coord)
        tmp.append(d)
        if d <= 6:
            receptorRes3.append(atom1['resNo'])
            nilotinibRes.append(atom2['resNo'])
        else:
            continue
            
            
receptorRes3_l = set(receptorRes3)
receptorRes3_l = [str(x) for x in receptorRes3_l]
" ".join(receptorRes3_l)