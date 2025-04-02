
from pywsgiapp.WSGIApp import createWSGIApp  

def requestHandler(url:str, requestHeaders:dict, postData:dict) -> dict:
    """
        If a file is present in the 'postData', it can be accessed using the provided key.
        The filename is available under the key 'filename', and the file content can be accessed 
        using the key 'content'.
        Example:
        postData = {
            'file': {
            'filename': 'example.txt',
            'content': b'Hello, World!'
            }
        }
        """
    if postData and 'file' in postData:
        fileName = postData['file']['filename']
        fileContent = postData['file']['content']
        with open(fileName, 'wb') as f:
            f.write(fileContent)
        response_body = f"File '{fileName}' saved successfully."
    else:
        response_body = "No file data received."            
    
    return {
        "responseCode": 200,
        "responseHeaders": {"Content-Type": "text/plain"},
        "responseBody": response_body
    }

app = createWSGIApp(requestHandler)

