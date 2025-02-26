from sys import stderr, exit, argv as Argv
from string import punctuation


if len(Argv) != 3:
    print("ERROR", file=stderr)
    exit(1)

length = 0
try:
    length = int(Argv[2])
except ValueError:
    print("ERROR", file=stderr)
    exit(1)

index = 0
input = [""]
output = []

for char in Argv[1]:
    if char in punctuation + " \t\n":
        input.append("")
        index += 1
    else:
        input[index] += char

output = [word for word in input if len(word) > length]

print(output)
