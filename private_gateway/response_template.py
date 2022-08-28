import json


def errorResponse(error_message: str, message="Error") -> dict:
    """ This function defines the custom 404 error message."""
    print({
            "message": "Creating Error Response Payload",
            "Error": error_message
        })

    responseData = {"status": "Error", "status_desc": error_message, "message": message}
    responseObject = {}
    responseObject['statusCode'] = 404
    responseObject["headers"] = {}
    responseObject["headers"]["Content-Type"] = 'application/json'
    responseObject['body'] = json.dumps(responseData)
    return responseObject

def successResponse() -> dict:
    """ This function defines the custom 200 success message."""
    print({
            "message": "Creating Success Response Payload",
            "status": "success"
        })

    responseData = {"status": "success"}
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject["headers"] = {}
    responseObject["headers"]["Content-Type"] = 'application/json'
    responseObject['body'] = json.dumps(responseData)
    return responseObject