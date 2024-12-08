import re

futureCommandsValid = True

f = open("C:/Users/joshu/OneDrive/Documents/GitHub/Cis-170-proj-5-github-desktop/advent-of-code-2024/dayThree/input.txt", "r")
commands = []
sum = 0
regex = "mul[\(][0-9]*[,][0-9]*[\)]|do\(\)|don't\(\)" # |(do\(\))|or(don't\(\))
for line in f:
    fileLine = line.strip("\n")
    lineMuls = re.findall(regex, fileLine)
    for command in lineMuls:
        commands.append(command)

print(commands)

for command in commands:
    if command == "do()":
        futureCommandsValid = True
    elif command == "don't()":
        futureCommandsValid = False
    elif futureCommandsValid and command.count("mul") == 1:
        stripedMul = command.strip("mul()")
        print(stripedMul)
        numsToMultiply = stripedMul.split(",")
        sum += int(numsToMultiply[0]) * int(numsToMultiply[1])

print("\n")
print(sum)