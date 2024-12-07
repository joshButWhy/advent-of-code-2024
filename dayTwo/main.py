f = open("C:/Users/joshu/OneDrive/Documents/GitHub/Cis-170-proj-5-github-desktop/advent-of-code-2024/dayTwo/numbers.txt", "r")
safeLevels = 0
isCurLineSafe = True
safeAfterRemoval = False

def isLevelSafe(level):
    curLineSorted = sorted(level)
    curLineReversed = sorted(level[:])[::-1]
    if (level != curLineSorted):
        if (level != curLineReversed):
            return False

    for x in range(1, len(level)):
        if abs(level[x] - level[x - 1]) < 1 or abs(level[x] - level[x - 1]) > 3:
            return False
    return True



for line in f:
    curLine = line.strip("\n")
    curLine = curLine.split(" ")
    for x in range(len(curLine)):
        curLine[x] = int(curLine[x])
    if (not isLevelSafe(curLine)):
        isCurLineSafe = False
    
    for x in range(len(curLine)):
        removalLine = curLine[:]
        removalLine.pop(x)
        if isLevelSafe(removalLine):
            safeAfterRemoval = True
    
    if (isCurLineSafe or safeAfterRemoval):
        safeLevels += 1
    isCurLineSafe = True
    safeAfterRemoval = False
print(safeLevels)

