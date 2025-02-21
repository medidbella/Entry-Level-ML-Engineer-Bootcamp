import sys

def formatter(input):
    if input.isupper():
        print(input.lower(), end="")
    else:
        print(input.upper(), end="")

i = len(sys.argv) - 1
while i > 0:
    j = len(sys.argv[i]) - 1
    while j >= 0:
        formatter(sys.argv[i][j])
        j -= 1
    i -= 1
    print(' ', end="")
print()
