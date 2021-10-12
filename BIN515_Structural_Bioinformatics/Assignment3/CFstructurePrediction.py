parameters = {'A':{'pa':142,'pb':83,'pturn':66},
              'R':{'pa':98,'pb':93,'pturn':95},
              'D':{'pa':101,'pb':54,'pturn':146},
              'N':{'pa':67,'pb':89,'pturn':156},
              'C':{'pa':70,'pb':119,'pturn':119},
              'E':{'pa':151,'pb':37,'pturn':74},
              'Q':{'pa':111,'pb':110,'pturn':98},
              'G':{'pa':57,'pb':75,'pturn':156},
              'H':{'pa':100,'pb':87,'pturn':95},
              'I':{'pa':108,'pb':160,'pturn':47},
              'L':{'pa':121,'pb':130,'pturn':59},
              'K':{'pa':114,'pb':74,'pturn':101},
              'M':{'pa':145,'pb':105,'pturn':60},
              'F':{'pa':113,'pb':138,'pturn':60},
              'P':{'pa':57,'pb':55,'pturn':152},
              'S':{'pa':77,'pb':75,'pturn':143},
              'T':{'pa':83,'pb':119,'pturn':96},
              'W':{'pa':108,'pb':137,'pturn':96},
              'Y':{'pa':69,'pb':147,'pturn':114},
              'V':{'pa':106,'pb':170,'pturn':50}}

def mean(x):
    return sum(x)/len(x)

def findStructure(sequence, structure):
"""Finds predicted helices and sheets based on prosperity values"""
    pars = {'alpha': (6,4,4, 'pa', 106, 70, 'pb', 103), 
                 'beta': (5,4,3, 'pb', 105, 83, 'pa', 105)}
    nucl, shift, condition, prosperity, maxi, mini, opposite, avg = pars[structure]
    structures = []
    for res in range(len(sequence)-shift):
        seed = sequence[res:res+nucl]
        maker = [x for x in seed if parameters[x][prosperity] > maxi]
        breaker = [x for x in seed if parameters[x][prosperity] < mini]
        if structure == 'alpha':
            indif = [x for x in seed if parameters[x][prosperity] >= 100 and parameters[x][prosperity] <= 101]
        else:
            indif = []
        if (len(maker) + len(indif)/2) >= condition and len(breaker) <= 1:
            ## print([res,res+nucl])
            seqCoor = []
            for res2 in range(res+nucl ,len(sequence)-shift):
                    seed2 = sequence[res2:res2+shift]
                    priProsp = [parameters[x][prosperity] for x in seed2]
                    secProsp = [parameters[x][opposite] for x in seed2]
                    mean_priProsp = mean(priProsp)
                    if mean_priProsp >= 100:
                        continue
                    else:
                        seqCoor.append(res2)
                        break
            if len(seqCoor) == 0:
                seqCoor.append(len(sequence))
            for res3 in range(res, shift, -1):
                seed3 = sequence[res3-shift:res3]
                priProsp = [parameters[x][prosperity] for x in seed3]
                secProsp = [parameters[x][opposite] for x in seed3]
                mean_priProsp = mean(priProsp)
                if mean_priProsp >= 100:
                    continue    
                else:
                    seqCoor.append(res3)
                    break
            if len(seqCoor) == 1:
                seqCoor.append(0)
            candidate = sequence[seqCoor[1]:seqCoor[0]]
            priProsp_candidate = [parameters[x][prosperity] for x in candidate]
            secProsp_candidate = [parameters[x][opposite] for x in candidate]
            mean_priProsp_candidate = mean(priProsp_candidate)
            mean_secProsp_candidate = mean(secProsp_candidate)
            if mean_priProsp_candidate > avg and mean_priProsp_candidate > mean_secProsp_candidate:
                structures.append(seqCoor[::-1])
    structures.sort(key = lambda x : x[0])
    return structures

def deduplicate(structure):
"""Removes the duplicated predictions"""
    dedup = []
    for s in structure:
        if not s in dedup:
            dedup.append(s)
    return dedup

def has_overlaps(range1, range2):
"""Returns boolean value of overlapping regions"""
    range1 = set(range(range1[0], range1[1]+1))
    range2 = set(range(range2[0], range2[1]+1))
    return len(range1.intersection(range2)) > 0

def overlap(range1, range2):
"""Returns the overlapping regions between two range"""
    range1 = set(range(range1[0], range1[1]+1))
    range2 = set(range(range2[0], range2[1]+1))
    
    un = range1.union(range2)
    mi = min(un)
    mx = max(un)
    
    return([mi,mx])


def mergeOverlaps(structure):
""""Merges the overlapping regions with respect to maximum and minimum values of residues""""
    overlapped = []
    overlaptrack = 0
    structure = deduplicate(structure)
    newStructure = structure[0]
    last = [len(structure) - 2, len(structure) -1]
    for i in range(len(structure)-1):
        #newStructure = structure[i]
        overlapping = has_overlaps(newStructure, structure[i+1])
        if  overlapping:
            newStructure = overlap(newStructure, structure[i+1])
            if not overlaptrack:
                overlaptrack = 1
                #print(i)
                if i in last:
                    overlapped.append(newStructure)
                
        else:
            overlapped.append(newStructure)
            newStructure = structure[i+1]
            overlaptrack = 0
            if i in last:
                overlapped.append(newStructure)
            
    return overlapped
            

def solveConflicts(a, b,sequence):
"""Finds overlapping regions between helices and sheets, returns the one with the greater average value, either helix or sheet"""
    to_delete_a = []
    to_delete_b = []
    for alpha in a:
        for beta in b:
            overlaps = has_overlaps(alpha, beta)
            if overlaps:
                mean_pa = mean([parameters[x]['pa'] for x in sequence[alpha[0]:alpha[1]]])
                mean_pb = mean([parameters[x]['pb'] for x in sequence[beta[0]:beta[1]]])
                if mean_pa > mean_pb:
                    to_delete_b.append(beta)
                else:
                    to_delete_a.append(alpha)
    to_delete_a = deduplicate(to_delete_a)
    to_delete_b = deduplicate(to_delete_b)
    
    for d in to_delete_a:
        i = a.index(d)
        del(a[i])
    for d in to_delete_b:
        i = b.index(d)
        del(b[i])
        
        
    return (a, b)
                

def CF(sequence):
"""Predicts the secondary structure of a protein given that its sequence by using Chou Fasman algorithm"""
    alphas = deduplicate(findStructure(sequence, 'alpha'))
    betas  = deduplicate(findStructure(sequence, 'beta'))
    
    alphas = mergeOverlaps(alphas)
    betas = mergeOverlaps(betas)
    
    alphas, betas = solveConflicts(alphas, betas, sequence)
    
    
    return (alphas, betas)                


### Parsing the observed secondary structures from PDB file

def parseHelices(line):
    return [int(line[21:25]), int(line[33:37])]
    

def parseSheets(line):
    return [int(line[22:26]), int(line[33:37])]
     

with open('/home/ece/Downloads/6O31_A.fasta.txt') as fasta:
    tmp = fasta.readlines()
    seq = "".join([x.strip() for x in tmp[1:]])
    
alfacik, betacik = CF(seq)

    

hList = []
sList = []

with open('/home/ece/Downloads/6o31.pdb') as pdbFile:
    for l in pdbFile:
        if l.startswith('HELIX'):
            hList.append(parseHelices(l))
        elif l.startswith('SHEET'):
            sList.append(parseSheets(l))

### Accuracy  calculation

alpharesidues = []
betaresidues = []
for i in alfacik:
    alpharesidues += [x+44 for x in list(range(i[0], i[1]+1))]
    
for i in betacik:
    betaresidues += [x+44 for x in list(range(i[0], i[1]+1))]
    
realalphas = []
realbetas = []
    
for i in hList:
    realalphas += list(range(i[0],i[1]+1))
    
for i in sList:
    realbetas  += list(range(i[0],i[1]+1))
    
correctalphas = 0
correctbetas  = 0
for res in realalphas:
    if res in alpharesidues:
        correctalphas += 1
        
for res in realbetas:
    if res in betaresidues:
        correctbetas += 1
        
accuracy = (correctalphas + correctbetas) / (len(realalphas)+len(realbetas)) * 100
