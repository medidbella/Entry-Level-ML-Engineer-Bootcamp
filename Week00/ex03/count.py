from sys import argv, stdin, stderr, exit
from string import punctuation


class Data:
    printableChars = 0
    upperChars = 0
    lowerChars = 0
    punctuationChars = 0
    spaces = 0


charsData = Data()


def counter(character):
    if character.isprintable():
        charsData.printableChars += 1
    if character.islower():
        charsData.lowerChars += 1
    if character.isupper():
        charsData.upperChars += 1
    if character.isspace():
        charsData.spaces += 1
    if character in punctuation:
        charsData.punctuationChars += 1


def text_analyzer(text=None):
    '''This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text.'''
    if not text:
        print("enter the text you want to analyze")
        text = stdin.readline()
    for character in text:
        counter(character)
    print(f"The text contains {charsData.printableChars} printable character(s):")
    print(f" - {charsData.upperChars} upper letter(s)")
    print(f" - {charsData.lowerChars} lower letter(s)")
    print(f" - {charsData.upperChars} punctuation mark(s)")
    print(f" - {charsData.spaces} space(s)")


if __name__ == "__main__":
    if len(argv) > 2:
        print("usage: python3.xx count.py <input>", file=stderr)
        exit(1)
    elif len(argv) == 2:
        text_analyzer(argv[1])
    else:
        print()
