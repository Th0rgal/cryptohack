content = input("input:").upper()
bruteforce = bool(input("bruteforce:").lower() == "true")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def shift_word(word, shift):
    output = ""
    for char in word:
        output += (
            alphabet[(alphabet.index(char) + shift) % len(alphabet)]
            if char in alphabet
            else char
        )
    return output


if not bruteforce:
    print(shift_word(content, int(input("shift:"))))
else:
    for shift in range(0, 26):
        print(shift_word(content, shift))
