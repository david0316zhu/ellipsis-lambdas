from public_gateway.public_gateway_function import lambda_handler as pub_lam


import base64
import json
from Cryptodome.Cipher import AES, PKCS1_v1_5
def encrypt_data(key: str, text: str) -> str:
    """Encrypt data payload to be sent to SCB Acquirer."""

    try:
        block_size = AES.block_size
        iv = "0" * AES.block_size
        # Pad forumla follows scb documentation
        padding = lambda s: s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size)

        cipher = AES.new(key.upper().encode(), AES.MODE_CBC, iv.encode())
        enc_string = cipher.encrypt(padding(text).encode())
        response = base64.b64encode(enc_string).decode()
        return response

    except Exception as e:
        raise Exception('Unable to encrypt payload.')
SECRET_KEY = "iGAJ40TzyuTn1tZWMK42pQvk16RVAqmx"
pl = "first_name=tom&last_name=lee&loan_amount=1000000&time_period=20&nric=t01234567a&asset_value=300000&monthly_income=6500"
encrypted_payload = encrypt_data(key=SECRET_KEY, text=pl)

payload = {
    "merchant_id": "1",
    "service": "risk_assessment",
    "enc": encrypted_payload

}

ret = pub_lam({"body": json.dumps(payload)}, 0)
print(ret)
