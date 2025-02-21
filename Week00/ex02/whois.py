from sys import argv, stderr, exit

if len(argv) > 2:
    print("Error: wrong number of argument",file=stderr)
    exit(1)

if len( argv) == 1:
    print()
    exit(0)
number = 0
try:
    number = int(argv[1]) 
except:
    print("Error: argument is not number", file=stderr)
    exit(1)
if number == 0:
    print("I'am Zero")
elif number % 2 != 0:
    print("I'am Odd")
else:
    print("I'am Even")

