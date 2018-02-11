from computingFrequencies import computingFreqs
from numberToPattern import numberToPattern

def clumpFinding(Genome, k, t, L):
    genomeList = list(Genome)
    frequentPatterns = []
    clump = []
    for i in range(4**k - 1 + 1):
        clump[i] = 0
    for i in range(len(genomeList) - L + 1):
        text = genomeList[i:i+L]
        frequencyArray = computingFreqs(text,k)
        for index in range(4**k-1+1):
            if frequencyArray[index] >= t:
                clump[index] = 1
    for i in range(4**k):
        if clump[i] == 1:
            pattern = numberToPattern(i,k)
            frequentPatterns.append(pattern)
    return frequentPatterns

def readData(filename):
    with open(filename, 'r') as f:
        Genome = f.readline()
        return Genome.strip()


if __name__ == "__main__":
    Genome = readData('dataset_4_5.txt')
    k = 10
    L = 519
    t = 20
    result = clumpFinding(Genome, k, t, L)
    print(result)