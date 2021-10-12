import sys

def chainSeparator(pdbFileName):
    """
    Inputs the pdbFile and returns 
    the chains as separated
    """
    chains = {}
    with open(pdbFileName) as pdbFile:
        for line in pdbFile:
            if line.startswith('ATOM'):
                currentChain = line[21]
                if currentChain in chains:
                    chains[currentChain].append(line)
                else:
                    chains[currentChain] = [line]
    return chains

chainDict = chainSeparator(sys.argv[1])

for chain in chainDict:
    with open(sys.argv[1]+'_chain'+chain+'.pdb', "w") as pdbFile:
        for line in chainDict[chain]:
            pdbFile.write(line)
        pdbFile.write("END\n")
