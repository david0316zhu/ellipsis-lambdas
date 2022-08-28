import json 
from .custom_trace import log_trace_message
from .utils import merchant_decryption_and_checks
from .response_template import errorResponse

def lambda_handler(event, context):
    """This function runs preliminary checks for merchant payloads"""
    try:
        body = json.loads(event["body"])
        print(body)
        #function to check whther client id is in database
        #check whether service match with client databse
        res = merchant_decryption_and_checks(payload=body)
        return res
    except Exception as e:
        log_trace_message()
        print(e.args)
        return errorResponse(error_message="Interal Error")