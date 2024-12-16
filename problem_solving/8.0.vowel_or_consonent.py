while True:
    letter = input("Enter a Letter : ")

    letter = letter.lower()

    if (
        letter == "a"
        or letter == "e"
        or letter == "i"
        or letter == "o"
        or letter == "u"
    ):
        print(f'"{letter}" is a Vowel')
    else:
        print(f'"{letter}" is a Consonent')
