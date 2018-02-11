import pdb

def patternMatch(Text, Pattern):
    pos =[]
    textList = list(Text)
    patternList = list(Pattern)
    for i in range(0,len(textList)):
        if textList[i:i+len(patternList)] == patternList:
            pos.append(str(i))
    return " ".join(pos)

def readData(filename):
    with open(filename, 'r') as f:
        Text = f.readline()
        return Text.strip()

if __name__ == "__main__":
    Text = readData('Vibrio_cholerae.txt')
    Pattern = "CTTGATCAT"
    result = patternMatch(Text, Pattern)
    print(result)
