f = open("/home/joshu/GitStuff/adventOfCode2024/dayTwo/numbers.txt", "r")
safeLevels = 0
for line in f:
    curLine = line.strip("\n")
    curLine = curLine.split(" ")
    print(curLine)
    curLineSorted = curLine.sort()
    print(curLineSorted)
    
    # curLineReversed = curLine[:].sort().reverse()
    # print(curLineReversed)
    print(curLine)
    if (curLine != curLineSorted or curLine != curLineReversed):
        continue
    safeLevels += 1
print(safeLevels)

