from sys import argv

def formatter(input):
    if input.isupper():
        print(input.lower(), end="")
    else:
        print(input.upper(), end="")

i = len(argv) - 1
while i > 0:
    j = len(argv[i]) - 1
    while j >= 0:
        formatter(argv[i][j])
        j -= 1
    i -= 1
    print(' ', end="")
print()
