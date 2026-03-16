from pywsgiapp.WSGIApp import createWSGIApp
import json


# ---------------------------------------------------------------------------
# Example 1: CORS disabled (corsConfig=None)
# No CORS headers are added to any response.
# ---------------------------------------------------------------------------

def requestHandler(url: str, requestHeaders: dict, postData: dict) -> dict:
    return {
        "responseCode": 200,
        "responseHeaders": {"Content-Type": "application/json"},
        "responseBody": json.dumps({"message": "CORS is disabled"})
    }

app_no_cors = createWSGIApp(requestHandler)


# ---------------------------------------------------------------------------
# Example 2: CORS enabled with required keys only
# Preflight OPTIONS requests return 200 with the provided headers.
# All other responses also include the CORS headers.
# ---------------------------------------------------------------------------

corsConfig_basic = {
    "enableCORS": True,
    "headers": [
        ("Access-Control-Allow-Origin", "*"),
        ("Access-Control-Allow-Methods", "GET, POST, OPTIONS"),
        ("Access-Control-Allow-Headers", "Content-Type, Authorization"),
    ]
}

app_basic_cors = createWSGIApp(requestHandler, corsConfig=corsConfig_basic)


# ---------------------------------------------------------------------------
# Example 4: CORS config provided but enableCORS=False
# corsConfig is validated, but no CORS headers are added to responses.
# Useful for toggling CORS off without removing the config.
# ---------------------------------------------------------------------------

corsConfig_disabled = {
    "enableCORS": False,
    "headers": [
        ("Access-Control-Allow-Origin", "*"),
        ("Access-Control-Allow-Methods", "GET, POST, OPTIONS"),
        ("Access-Control-Allow-Headers", "Content-Type"),
    ]
}

app_cors_off = createWSGIApp(requestHandler, corsConfig=corsConfig_disabled)
