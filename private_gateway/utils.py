import requests
import os
from urllib import parse
from .custom_trace import log_trace_message
from .response_template import errorResponse, successResponse
from .enc import decrypt_data
#GS_INTERNAL = os.getenv("GS_INTERNAL")
SECRET_KEY = "iGAJ40TzyuTn1tZWMK42pQvk16RVAqmx"
def merchant_decryption_and_checks(payload):
    """This function decrypts payload and check whether payloads parameters are all proper"""
    try:

        merchant_id = payload.get("merchant_id")
        if not merchant_id:
            return errorResponse(error_message="Merchant ID parameter not found")
        
        encrypted_data = payload.get("enc")
        if not encrypted_data:
            return errorResponse(error_message="Encrypted data parameter not found")
        
        plain_data = decrypt_data(key=SECRET_KEY, text=encrypted_data, clientid=merchant_id)
        if not plain_data:
            return errorResponse(error_message="Decryption Error")
        data_dict = parse.parse_qs(plain_data)
        if not check_parameters(data=data_dict):
            return errorResponse(error_message="Parameters invalid")
        
        #res = requests.post(url=GS_INTERNAL, json=data_dict)
        res = {"status": 200, "body": {"message": "request received"}}
        if res["status"] == 200:
            return successResponse()
        
        return errorResponse("Internal Error")

    except Exception as e:
        log_trace_message()
        print(e.args)
        return errorResponse("Internal Error")


def check_parameters(data: dict):
    try:
        
        params = ["first_name", "last_name", "loan_amount", "time_period", "nric", "asset_value", "monthly_income"]
        for param in data:
            if param not in params:
                print(param)
                return False
        return True
    
    except Exception as e:
        log_trace_message()
        print(e.args)
        return False

