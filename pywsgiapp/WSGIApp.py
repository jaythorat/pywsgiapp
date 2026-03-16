import logging

from pywsgiapp.config.config import Config
from pywsgiapp.support.parseEnviron import ParseEnviron as Pe


class WsgiApp:

    def __init__(self):
        self.dConfig = Config()
        if self.dConfig.appLoggingStatus():
            logging.basicConfig(
                filename="logs/wsgiLog.log", level=logging.INFO)

    def processRequestData(self, environ):
        pe = Pe(environ)
        url = pe.getUrl()
        requestHeaders = pe.getRequestHeaders()
        if "CONTENT_TYPE" in requestHeaders:
            postData = pe.getPostData()
        else:
            postData = {}
        return url, requestHeaders, postData

    def processResponse(self, resp):
        statusCode = str(resp["responseCode"])
        responseHeader = resp["responseHeaders"]
        encodeResponse = str(resp["responseBody"]).encode("UTF-8")
        responseHeaderList = [(key, value)
                              for key, value in responseHeader.items()]
        return statusCode, responseHeaderList, encodeResponse
    
    def validateCORSCong(self, corsConfig):
        if not isinstance(corsConfig, dict):
            raise TypeError("corsConfig must be a dictionary")

        # --- Required keys ---
        if "enableCORS" not in corsConfig:
            raise KeyError("corsConfig missing required key: 'enableCORS'")
        if not isinstance(corsConfig["enableCORS"], bool):
            raise TypeError("'enableCORS' must be a bool")

        if "headers" not in corsConfig:
            raise KeyError("corsConfig missing required key: 'headers'")
        if not isinstance(corsConfig["headers"], list):
            raise TypeError("'headers' must be a list")
        for i, header in enumerate(corsConfig["headers"]):
            if not isinstance(header, tuple) or len(header) != 2:
                raise ValueError(f"'headers[{i}]' must be a tuple of (name, value), got: {repr(header)}")
            name, value = header
            if not isinstance(name, str) or not name.strip():
                raise ValueError(f"'headers[{i}]' name must be a non-empty string, got: {repr(name)}")
            if not isinstance(value, str):
                raise ValueError(f"'headers[{i}]' value must be a string, got: {repr(value)}")
        return True


    def logInfo(self, data):
        logging.info(data)


def createWSGIApp(reqestHandler, corsConfig: dict = None):
    """
    Create a WSGI application.

    Args:
        reqestHandler (function): A function that processes the request and returns a dictionary with:
            - responseCode (int): HTTP status code.
            - responseHeaders (dict): Headers to include in the response.
            - responseBody (str): The response body.
        corsConfig (dict, optional): CORS configuration. If None, CORS headers are not added.
            Required keys:
                - enableCORS (bool): Whether to enable CORS.
                - headers (list): List of (name, value) tuples to send as CORS headers.

    Returns:
        function: A WSGI application callable.
    """
    wsgiapp = WsgiApp()

    cors_enabled = False
    cors_headers = []

    if corsConfig is not None:
        wsgiapp.validateCORSCong(corsConfig)
        cors_enabled = corsConfig["enableCORS"]
        cors_headers = corsConfig["headers"] if cors_enabled else []

    def app(environ, start_response):
        if cors_enabled and environ["REQUEST_METHOD"] == "OPTIONS":
            start_response("200 OK", cors_headers)
            return [b""]

        url, requestHeaders, postData = wsgiapp.processRequestData(environ)
        resp = reqestHandler(url, requestHeaders, postData)
        statusCode, responseHeaderList, encodeResponse = wsgiapp.processResponse(resp)
        start_response(statusCode, responseHeaderList + cors_headers)
        return [encodeResponse]

    return app
