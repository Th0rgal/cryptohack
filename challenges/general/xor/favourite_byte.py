from pwn import xor

text = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

key = bytes([ 109, 121, 88, 79, 82, 107, 101, 121 ]).decode()
print(key)


text = xor(text, key)
print(text)