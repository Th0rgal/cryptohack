content = input("input:").upper()
shift = int(input("shift:"))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
output = ""
for char in content:
    output += alphabet[alphabet.index(char)+shift]
print(output)