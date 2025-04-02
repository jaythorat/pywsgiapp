from pywsgiapp.WSGIApp import createWSGIApp  

def requestHandler(url:str, requestHeaders:dict, postData:dict) -> dict:
    
    response_body = f"Received URL: {url}, Headers: {requestHeaders}, Post Data: {postData}"
    return {
        "responseCode": 200,
        "responseHeaders": {"Content-Type": "text/plain"},
        "responseBody": response_body
    }

app = createWSGIApp(requestHandler)

