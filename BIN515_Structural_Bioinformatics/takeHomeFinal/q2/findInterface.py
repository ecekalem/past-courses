import os
import pandas as pd
import re

findIndices = lambda x,l: [i for i in range(len(l)) if l[i] == x]

def findChain(complexs, chain1, chain2):
    l_ch1 = len(chain1)
    l_ch2 = len(chain2)
    
    ch1_firstLast = [chain1["Residue"][0], chain1["Residue"][l_ch1-1]]
    ch2_firstLast = [chain2["Residue"][0], chain2["Residue"][l_ch2-1]]
    ch1_firstLast_n= [chain1["resNum"][0], chain1["resNum"][l_ch1-1]]
    ch2_firstLast_n= [chain2["resNum"][0], chain2["resNum"][l_ch2-1]]
    ch1_check = (complexs["resNum"][0] == ch1_firstLast_n[0]) and (complexs["resNum"][l_ch1-1] == ch1_firstLast_n[1]) and (complexs["Residue"][0] == ch1_firstLast[0]) and (complexs["Residue"][l_ch1-1] == ch1_firstLast[1])
    if ch1_check:
        return chain1
    else:
        return chain2
    
    
def findInterface(complexs, firstChain, secondChain, chainNames):
    firstChain_complex = complexs.iloc[:len(firstChain)]
    secondChain_complex = complexs.iloc[len(firstChain):]
    
    firstChainInterface = list(firstChain["resNum"][firstChain["Ratio(%)"] - firstChain_complex["Ratio(%)"] > 1].values)
    secondChainInterface = list(secondChain["resNum"][secondChain["Ratio(%)"].values - secondChain_complex["Ratio(%)"].values > 1])
    
    interfaces = {}
    interfaces[chainNames[0]] = firstChainInterface
    interfaces[chainNames[1]] = secondChainInterface
    
    return interfaces

def interfacePropensity(masterDict):
    
    residCounts = {}
    for pdb in masterDict:
        complexs = masterDict[pdb]['complex']
        interfaces = masterDict[pdb]['interfaces']
        firstChain = masterDict[pdb]['firstChain']
        isInterface = [False for i in range(len(complexs))]
        newComplexs = None
        for chain in interfaces:
            if chain == firstChain:
                thisInterface = interfaces[chain]
                thisChain_complex = complexs.iloc[:len(masterDict[pdb][firstChain])]
                ##print(thisChain_complex.head())
                tmp = [x in thisInterface for x in thisChain_complex['resNum'] ]
                thisChain_complex["isInterface"] = tmp
                if newComplexs != None:
                    newComplexs.append(thisChain_complex)
                else:
                    newComplexs = thisChain_complex.copy()
            
        for index,row in newComplexs.iterrows():
            resid = row['Residue']
            intf = row['isInterface']
            key = {True: 'intf', False: 'nointf'}[intf]
            if resid in residCounts:
                residCounts[resid][key] += 1
            else:
                residCounts[resid] = {'intf': 0, 'nointf': 0}
                residCounts[resid][key] += 1
    
    
    return residCounts
    
pdbList = os.listdir("./pdbfiles")
dict1 = {}
for f in pdbList:
    os.chdir("./pdbfiles/"+ f)
    tableList = [x for x in os.listdir() if x.endswith('.txt')]
    pdbDict = {}
    for t in tableList:
        table = []
        with open(t) as tb:              
             for l in tb:
                if l.startswith("<td><pre>"):
                    l = l.strip()
                    l = l.replace("<td><pre>","")
                    l = l.replace("</pre></td>","")
                    l = l.split()
                    if len(l) > 0 and l[0].startswith("--"):
                        break
                    table.append(l)
                    
        pdbDict[t] = table
    dict1[f] = pdbDict
    os.chdir('../../')
    print(os.getcwd())


dict2 = {}

for pdb in dict1:
    dict2[pdb] = {}
    for asa in dict1[pdb]:
        table = dict1[pdb][asa]
        header = table[1]
        header = [header[0], "resNum" ] + header[1:]
        #print(header)
        df = pd.DataFrame(table[2:], columns=header)
        df["Ratio(%)"] = pd.to_numeric(df['Ratio(%)'])
        #print(df.head())
        this = re.findall(r"chain[A-Z]", asa)
        if len(this) == 0:
            key = 'complex'
        else:
            key = this[0]
        dict2[pdb][key] = df
        

for pdb in dict2:
    chains = [x for x in dict2[pdb].keys() if x != "complex"]
    df_complex = dict2[pdb]['complex']
    chainsList = [dict2[pdb][x] for x in chains]
    firstChain = findChain(df_complex, chainsList[0], chainsList[1])
    if id(firstChain) == id(chainsList[0]):
        firstChain = chainsList[0]
        secondChain = chainsList[1]
        ##firstChainName = chains[0]
        ##secondChainName = chains[1]
    
    else:
        firstChain = chainsList[1]
        secondChain = chainsList[0]
        ##firstChainName = chains[1]
        ##secondChainName = chains[0]
        chains = chains[::-1]
        
    interfaces = findInterface(df_complex, firstChain, secondChain, chains)
    dict2[pdb]['interfaces'] = interfaces
    dict2[pdb]['firstChain'] = chains[0]
   
    
    ##firstChain = lens.index(breakPoint[0]+1)
    ## print("for prot " + pdb + " firstchain is " + str(firstChain))
    
    
props = interfacePropensity(dict2)

denom1 = sum([props[x]['intf'] for x in props])
denom2 = sum([props[x]['intf'] + props[x]['nointf'] for x in props])

propensities = {}

for aa in props:
    numer = (props[aa]['intf'] / (props[aa]['intf'] + props[aa]['nointf']))
    denom = (denom1 / denom2)
    propensities[aa] = numer/denom
    
    
groups = {
    'small': ['GLY', 'ALA'],
    'hydrophobic': ['ALA', 'PRO', 'VAL', 'LEU'],
    'negative': ['GLU', 'ASP'],
    'positive': ['LYS', 'ARG'],
    'polar':  ['GLN', 'ASN', 'THR','SER','TRP', 'HIS', 'TYR'],
    'aromatic': ['TRP', 'HIS', 'TYR', 'PHE']

}
group_propensities = {}

for group in groups:
    numer = sum([props[aa]['intf'] for aa in groups[group]]) / sum([props[aa]['intf'] + props[aa]['nointf'] for aa in groups[group]])
    denom = (denom1 / denom2)
    group_propensities[group] = numer / denom
    
   
tmp_a = dict2["3I7N"]['chainA']
tmp = dict2['3I7N']['complex']
tmp_b = dict2['3I7N']['chainB']
tmp_findChain = findChain(tmp, tmp_a, tmp_b)

"protein and chain A and resid " + " ".join(dict2['3HIZ']['interfaces']['chainA'])
"protein and chain B and resid " + " ".join(dict2['3HIZ']['interfaces']['chainB'])

with open("/home/ece/Desktop/structuralBioinformatics/FinalTakeHome/q2/c/aa_propensities.csv", "w") as csvf:
    for aa in propensities:
        csvf.write(",".join([aa,str(round(propensities[aa],3))]) + "\n")
        
with open("/home/ece/Desktop/structuralBioinformatics/FinalTakeHome/q2/c/group_propensities.csv", "w") as csvf:
    for group in group_propensities:
        csvf.write(",".join([group,str(round(group_propensities[group],3))]) + "\n")