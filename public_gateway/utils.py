import requests
import os
from db_interact import get_merchant_services, get_db_connection
from custom_trace import log_trace_message
from response_template import errorResponse

RISK_ASSESSMENT_URL = os.getenv("RISK_ASSESSMENT_URL")

def merchant_checks(payload):
    """This function checks whether the incoming merchant payload is correct"""
    try:

        merchant_id = payload.get("merchant_id")
        if not merchant_id:
            return errorResponse(error_message="Merchant ID parameter not found")
        required_service = payload.get("service")
        if not required_service:
            return errorResponse(error_message="Service parameter not found")
        connection = get_db_connection()
        if not connection:
            return errorResponse(error_message="Database Connection Failure")
        cursor = connection.cursor()
        
        merchant_data = get_merchant_services(cursor=cursor, merchant_id=merchant_id)
        cursor.close()
        connection.close()
        if not merchant_data:
            return errorResponse(error_message="Merchant Data not found")
        service_status = merchant_data.get(required_service)
        if not service_status:
            return errorResponse(error_message="Service Invalid")
        if service_status == "LIVE":
            resp = None
            if required_service == "risk_assessment":
                resp = requests.post(url=RISK_ASSESSMENT_URL, json=payload)

            elif required_service == "currency_exchange":
                resp = requests.post(url=RISK_ASSESSMENT_URL, json=payload)

            if not resp:
                return resp

            return errorResponse(error_message="Response Timeout")
        return errorResponse("Service not LIVE")
    except Exception as e:
        log_trace_message()
        print(e.args)
        return errorResponse("Internal Error")
