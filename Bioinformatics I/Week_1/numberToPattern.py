import pdb

def numberToSymbol(number):
    global symbol
    if number == 0:
        symbol = "A"
    elif number == 1:
        symbol = "C"
    elif number == 2:
        symbol = "G"
    elif number == 3:
        symbol = "T"
    return symbol

def numberToPattern(index,k):
    if k == 1:
        return numberToSymbol(index)
    quotient = index/4
    remainer = index % 4
    symbol = numberToSymbol(remainer)
    prefixPattern = numberToPattern(quotient,k-1)
    return prefixPattern + symbol

def readData(filename):
    with open(filename, 'r') as f:
        index = f.readline()
        k = f.readline()
        return int(index), int(k)

if __name__ == "__main__":
    index, k = readData('dataset.txt')
    result = numberToPattern(index,k)
    print(result)