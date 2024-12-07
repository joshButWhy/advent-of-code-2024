f = open("/home/joshu/GitStuff/adventOfCode2024/dayOne/numbers.txt")

# Part One
list1 = []
list2 = []
sum = 0

for line in f:
    curLine = line.split("   ")
    print(curLine)
    list1.append(curLine[0])

    list2.append(curLine[1].strip("\n"))

list1.sort()
list_1_reversed = list1[:].reverse()
list2.sort()
list_2_reversed = list2[:].reverse()


for x in range(len(list1)):
    sum += abs(int(list2[x]) - int(list1[x]))
print(list1)
print(sum)

similarity = 0

for x in range(len(list1)):
    num = list1[x]
    occurence = 0
    for y in range(len(list2)):
        if list2[y] == num:
            occurence += 1

    similarity += int(num) * occurence

print("\n")
print(similarity)


