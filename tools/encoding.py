import base64
from Crypto.Util.number import long_to_bytes

def ascii_to_string():
    ascii_codes = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
    output = ""
    for ascii_code in ascii_codes:
        output += chr(ascii_code)
    print(output)

def hex_to_string():
    hexa = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
    print(bytearray.fromhex(hexa).decode())

def b64_to_string():
    input_bytes = bytearray.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")
    print(base64.b64encode(input_bytes))