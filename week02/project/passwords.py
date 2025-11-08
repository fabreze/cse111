"""
Author: Fabrizio Caballero
Enchancements: I added a message that tells the user what they have to do to increase their strength score based on what characters they need to add to their password.
"""
LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]

def main():
    is_running = True
    print("Welcome to the Company Password Strength Checker! Please update any company passwords that have a strength lower than 5.\n" \
    "Enter Q at any time to exit the program\n")
    while(is_running):
        password = input("Type in a password to check its strength: ")
        if password.lower() == 'q':
            is_running = False
            print("Thanks for using the program, have a great day!")
        else:
            strength = password_strength(password)
            print(f"\nYour password has a strength score of {strength}\n")
    pass

def word_in_file(word, filename, case_sensitive=False):
    word_in_file = False
    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            content = line.strip()
            if case_sensitive:
                if word == content:
                    word_in_file = True
            else:
                lowercase_word = word.lower()
                if lowercase_word == content:
                    word_in_file = True
    return word_in_file

def word_has_character(word, character_list):
    word_has_character = False
    for character in character_list:
        if character in word:
            word_has_character = True
    return word_has_character

def word_complexity(word):
    word_complexity = 0
    if word_has_character(word, LOWER):
        word_complexity += 1
    else:
        print("\n!!! Add a lowercase letter to the password to increase it's strength !!!")

    if word_has_character(word, UPPER):
        word_complexity += 1
    else:
        print("\n!!! Add an uppercase letter to the password to increase it's strength !!!")

    if word_has_character(word, DIGITS):
        word_complexity += 1
    else:
        print("\n!!! Add a digit to the password to increase it's strength !!!")

    if word_has_character(word, SPECIAL):
        word_complexity += 1
    else:
        print("\n!!! Add a special character to the password to increase it's strength !!!")

    return word_complexity

def password_strength(password, min_length=10, strong_length=16):
    password_strength = 0
    if word_in_file(password, "wordlist.txt"):
        print("\nPassword is a dictionary word and is not secure.\n")

    elif word_in_file(password,"toppasswords.txt", True):
        print("\nPassword is a commonly used password and is not secure.\n")

    elif len(password) < min_length:
        print("\nPassword is too short and is not secure.\n")
        password_strength = 1

    elif len(password) > strong_length: 
        print("\nPassword is long, length trumps complexity this is a good password.\n")
        password_strength = 5
    else:
        password_strength = 1 + word_complexity(password)
    return password_strength

__name__ = "__main__"

if __name__ == "__main__":
    main()