# encript and decript text with base64

# import necessary modules

import base64
from cmath import e

def encode_data(plain_text):
    # convert pain_text and encode it
    plain_text = plain_text.encode()
    # encode plain_text
    cipher_text = base64.b64encode(plain_text)
    # convert encoded text back to string
    cipher_text = cipher_text.decode()
    return cipher_text
def decode_data(cipher_text):
    # decode cipher_text
    plain_text = base64.b64decode(cipher_text)
    plain_text = plain_text.decode()
    return plain_text
method = input("do you wish to encode or decode your data(e/d)? ").lower()

message = input("what is the message? ")

if method[0] == "e":
   print(encode_data(message))
elif method[0] == "d":
    print(decode_data(message))
else:
    # if method wasnt e or d print error
    print("wrong method selected: choose encode or decode")