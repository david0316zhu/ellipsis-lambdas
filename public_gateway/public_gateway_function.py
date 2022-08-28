import json 
from .custom_trace import log_trace_message
from .utils import merchant_checks

def lambda_handler(event, context):
    """This function runs preliminary checks for merchant payloads"""
    try:
        body = json.loads(event["body"])
        #function to check whther client id is in database
        #check whether service match with client databse
        res = merchant_checks(body)
        return res
    except Exception as e:
        log_trace_message()
        print(e.args)