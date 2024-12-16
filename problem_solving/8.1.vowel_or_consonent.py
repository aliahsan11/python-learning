vowel = ["a", "e", "i", "o", "u"]

while True:
    letter = input("Enter a Letter : ")

    letter = letter.lower()

    if letter in vowel:
        print(f'"{letter}" is a Vowel')
    else:
        print(f'"{letter}" is a Consonent')
