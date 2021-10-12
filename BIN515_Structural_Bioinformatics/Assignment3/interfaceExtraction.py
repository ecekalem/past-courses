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


chainU = []
chainP = []

# parsing the pdb file and appending the different chains to different lists
with open('/home/ece/Downloads/4zks.pdb') as f:
    for line in f:
        if line.startswith('ATOM'):
            xd = parseLine(line)
            if xd['chainid'] == 'U':
                chainU.append(line)
            else:
                chainP.append(line)
## Writing different chains to different files            
with open('/home/ece/Downloads/4zksChainU.pdb', 'w') as f:
    for line in chainU:
        f.write(line)
    f.write("END\n")
        
with open('/home/ece/Downloads/4zksChainP.pdb', 'w') as f:
    for line in chainP:
        f.write(line)
    f.write("END\n")