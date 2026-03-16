# Examples for `pywsgiapp`

This document contains examples demonstrating how to use the `pywsgiapp`.

---

## Table of Contents

1. [Basic WSGI Application](#example-1-basic-wsgi-application)
2. [JSON Response Application](#example-2-json-response-application)
3. [Save Received File](#example-3-save-received-file)
4. [CORS — Disabled (no corsConfig)](#example-4-cors--disabled-no-corsconfig)
5. [CORS — Enabled](#example-5-cors--enabled)
6. [CORS — Config provided but disabled](#example-6-cors--config-provided-but-disabled)

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

---

## Example 4: CORS — Disabled (no corsConfig)

No `corsConfig` is passed. No CORS headers are added to any response.

### Code

```python
from pywsgiapp.WSGIApp import createWSGIApp

def requestHandler(url: str, requestHeaders: dict, postData: dict) -> dict:
    return {
        "responseCode": 200,
        "responseHeaders": {"Content-Type": "text/plain"},
        "responseBody": "CORS is disabled"
    }

app = createWSGIApp(requestHandler)
```

---

## Example 5: CORS — Enabled

Preflight `OPTIONS` requests are handled automatically and all responses include the provided CORS headers.

### `corsConfig` keys

| Key          | Type   | Description                                      |
|--------------|--------|--------------------------------------------------|
| `enableCORS` | `bool` | Set to `True` to enable CORS                     |
| `headers`    | `list` | List of `(header-name, header-value)` tuples     |

### Code

```python
from pywsgiapp.WSGIApp import createWSGIApp
import json

corsConfig = {
    "enableCORS": True,
    "headers": [
        ("Access-Control-Allow-Origin", "*"),
        ("Access-Control-Allow-Methods", "GET, POST, OPTIONS"),
        ("Access-Control-Allow-Headers", "Content-Type, Authorization"),
    ]
}

def requestHandler(url: str, requestHeaders: dict, postData: dict) -> dict:
    return {
        "responseCode": 200,
        "responseHeaders": {"Content-Type": "application/json"},
        "responseBody": json.dumps({"message": "CORS enabled"})
    }

app = createWSGIApp(requestHandler, corsConfig=corsConfig)
```

---

## Example 6: CORS — Config provided but disabled

`corsConfig` is passed and validated, but `enableCORS` is `False`. No CORS headers are added to responses. Useful for toggling CORS off without removing the config.

### Code

```python
from pywsgiapp.WSGIApp import createWSGIApp

corsConfig = {
    "enableCORS": False,
    "headers": [
        ("Access-Control-Allow-Origin", "*"),
        ("Access-Control-Allow-Methods", "GET, POST, OPTIONS"),
        ("Access-Control-Allow-Headers", "Content-Type"),
    ]
}

def requestHandler(url: str, requestHeaders: dict, postData: dict) -> dict:
    return {
        "responseCode": 200,
        "responseHeaders": {"Content-Type": "text/plain"},
        "responseBody": "CORS toggled off"
    }

app = createWSGIApp(requestHandler, corsConfig=corsConfig)
```