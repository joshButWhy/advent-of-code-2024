f = open("C:/Users/joshu/OneDrive/Documents/GitHub/Cis-170-proj-5-github-desktop/advent-of-code-2024/daySeven/numbers.txt", "r")

for line in f:
    fileLine = line.strip("\n")
    workingLine = list(fileLine)
    
    workingLine.remove(":")

    splitableLine = "".join(workingLine)
    lineArr = splitableLine.split(" ")
    print(lineArr)