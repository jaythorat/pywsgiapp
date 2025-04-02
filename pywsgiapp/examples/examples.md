# Examples for `pywsgiapp`

This document contains examples demonstrating how to use the `pywsgiapp`.

---

## Example 1: Basic WSGI Application

The following example demonstrates how to create a simple WSGI application using `pywsgiapp`.

### Code

```python
from pywsgiapp.WSGIApp import createWSGIApp  

# Define a request handler function
def requestHandler(url: str, requestHeaders: dict, postData: dict) -> dict:
    response_body = f"Received URL: {url}, Headers: {requestHeaders}, Post Data: {postData}"
    return {
        "responseCode": 200,
        "responseHeaders": {"Content-Type": "text/plain"},
        "responseBody": response_body
    }

# Create the WSGI application
app = createWSGIApp(requestHandler)
```


## Example 2: JSON Response Application

The following example demonstrates how to return a JSON response using `pywsgiapp`.

### Code

```python
from pywsgiapp.WSGIApp import createWSGIApp
import json

# Define a request handler function
def requestHandler(url: str, requestHeaders: dict, postData: dict) -> dict:
    response_body = {
        "url": url,
        "headers": requestHeaders,
        "postData": postData
    }
    return {
        "responseCode": 200,
        "responseHeaders": {"Content-Type": "application/json"},
        "responseBody": json.dumps(response_body)
    }

# Create the WSGI application
app = createWSGIApp(requestHandler)
```



## Example 3: Save Received File

The following example demonstrates how to handle file uploads and save the file using `pywsgiapp`.

### Code

```python
from pywsgiapp.WSGIApp import createWSGIApp

# Define a request handler function
def requestHandler(url: str, requestHeaders: dict, postData: dict) -> dict:
    if "file" in postData:
        file_data = postData["file"]
        with open("uploaded_file", "wb") as f:
            f.write(file_data)
        response_body = "File uploaded successfully!"
    else:
        response_body = "No file uploaded."

    return {
        "responseCode": 200,
        "responseHeaders": {"Content-Type": "text/plain"},
        "responseBody": response_body
    }

# Create the WSGI application
app = createWSGIApp(requestHandler)
```