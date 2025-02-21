from sys import argv, stdin
from string import punctuation

class Data:
    printableChars = 0
    upperChars = 0
    lowerChars = 0
    punctuationChars = 0
    spaces = 0

myData = Data()

def counter(character):
    if character.isprintable():
        myData.printableChars += 1
    if character.islower():
        myData.lowerChars += 1
    if character.isupper():
        myData.upperChars += 1
    if character.isspace():
        myData.spaces += 1
    if character in punctuation:
        myData.punctuationChars += 1


def text_analyzer(text = None):
    if not text:
        print("enter the text you want to analyze")
        text = stdin.readline()
    for character in text:
        counter(character)
    print(f"The text contains {myData.printableChars} printable character(s):")
    print(f" - {myData.upperChars} upper letter(s)")
    print(f" - {myData.lowerChars} lower letter(s)")
    print(f" - {myData.upperChars} punctuation mark(s)")
    print(f" - {myData.spaces} space(s)")

if len(argv) == 2:
    text_analyzer(argv[1])