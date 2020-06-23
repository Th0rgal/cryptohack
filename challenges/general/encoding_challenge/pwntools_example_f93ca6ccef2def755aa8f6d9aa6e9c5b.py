from pwn import * # pip install pwntools
import json, base64, codecs
from Crypto.Util.number import long_to_bytes

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

while True:
    received = json_recv()
    encoding = received["type"]
    encoded = received["encoded"]

    if encoding == "base64":
        output = base64.b64decode(encoded).decode() # wow so encode
    elif encoding == "hex":
        output = bytearray.fromhex(encoded).decode() 
    elif encoding == "rot13":
        output = codecs.decode(encoded, 'rot_13')
    elif encoding == "bigint":
        output = long_to_bytes(int(encoded, 16)).decode()
    elif encoding == "utf-8":
        output = "".join([chr(b) for b in encoded])

    print(output)

    to_send = {
        "decoded": output
    }
    json_send(to_send)



