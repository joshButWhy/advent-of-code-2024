
def getInputText(inputDir="C:/Users/joshu/OneDrive/Documents/GitHub/Cis-170-proj-5-github-desktop/advent-of-code-2024/dayFour/input.txt"):
    arr = []
    
    f = open(inputDir, "r")
    for line in f:
        # process each line
        fileLine = line.strip("\n")
        fileLineArr = list(fileLine)
        arr.append(fileLineArr)
    return arr

inputDir = "C:/Users/joshu/OneDrive/Documents/GitHub/Cis-170-proj-5-github-desktop/advent-of-code-2024/dayFour/input.txt"
wordCount = 0
wordSearch = getInputText(inputDir)


def numWordInWordSearch(xIndex, yIndex, word="XMAS"):
    count = 0
    #check upwards
    if yIndex - len(word) >= -1:
        for y in range(yIndex, yIndex + 1 - len(word))
            
    #check upper-right
    if :
    #check right
    if :
    #check downward-right
    if :
    #check downward
    if :
    #check downward-left
    if :
    #check left
    if :
    #check upper-left
    if :
    
    return count

for y in range(len(wordSearch)):
    for x in range(len(wordSearch[0])):
        if wordSearch[y][x] == "X":
           wordCount += numWordInWordSearch(x, y)


print(len(wordSearch) * len(wordSearch[0]))
print(wordCount)