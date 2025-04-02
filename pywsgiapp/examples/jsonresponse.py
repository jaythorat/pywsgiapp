from pywsgiapp.WSGIApp import createWSGIApp
import json


def requestHandler(url: str, requestHeaders: dict, postData: dict) -> dict:
    data = {
        "name": "John Doe",
        "age": 30,
        "phone": None,
        "is_student": False,
        "courses": ["Math", "Science", "History"],
        "address": {
            "street": "123 Main St",
            "city": "New York",
            "state": "NY"
        },
    }
    response_body = json.dumps(data) # This will be a JSON string 
    
    return {
        "responseCode": 200,
        "responseHeaders": {"Content-Type": "text/plain"},
        "responseBody": response_body
    }

app = createWSGIApp(requestHandler)
