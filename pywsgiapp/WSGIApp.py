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

    def logInfo(self, data):
        logging.info(data)


def createWSGIApp(reqestHandler):
    """
    Create a WSGI application.

    Args:
        request_handler (function): A function that processes the request and returns a dictionary:
            Parameters:
            - url (str): The URL of the request.
            - requestHeaders (dict): A dictionary of request headers.
            - postData (dict): The parsed data from the request body
            Returns:
            - responseCode (int): The HTTP status code of the response.
            - responseHeaders (dict): A dictionary of headers to include in the response.
            - responseBody (str): The body of the response.

    Returns:
        function: A WSGI application callable.
    """
    def app(environ, start_response):
        wsgiapp = WsgiApp()
        url, requestHeaders, postData = wsgiapp.processRequestData(environ)
        resp = reqestHandler(url, requestHeaders, postData)
        statusCode, responseHeaderList, encodeResponse = wsgiapp.processResponse(
            resp)
        start_response(statusCode, responseHeaderList)
        return [encodeResponse]
    return app
