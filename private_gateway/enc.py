import base64
import os
from Cryptodome.Cipher import AES, PKCS1_v1_5
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from .custom_trace import log_trace_message
import json



def decrypt_data(key: str, text: str, clientid: str) -> str:
    """decrypt aes 256"""
    try:
        print({
            "Client ID": clientid,
            "message": "Decrypting Data"
        })
        _unpad = lambda s: s[0:-ord(s[-1])]
        iv = "0" * AES.block_size
        decodedStr = base64.b64decode(text)
        dec = AES.new(key.upper().encode(), AES.MODE_CBC, iv.encode())
        processedtext = dec.decrypt(decodedStr)
        decStr = _unpad(processedtext.decode())
        print({
            "Client ID": clientid,
            "message": f"Decrypted String: {decStr}"
        })
        return decStr
    except Exception as e:
        print({"Client ID": clientid, "message": e.args})
        log_trace_message()
        return None