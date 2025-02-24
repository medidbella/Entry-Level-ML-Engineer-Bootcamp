from sys import stderr, exit, argv
from string import punctuation
import re

if len(argv) != 3:
	print("ERROR", file=stderr)
	exit(1)

length = 0
try:
	length = int(argv[2])
except ValueError:
	print("ERROR", file=stderr)
	exit(1)

index = 0
input = [""]
output = []

for char in argv[1]:
	if char in punctuation + " \t\n":
		input.append("")
		index+=1
	else:
		input[index] += char

output = [word for word in input if len(word) > length]

print(output)