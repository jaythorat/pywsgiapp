import json
from pywsgiapp.support.parseMultipartForm import ParseMultipartFormdata as pmf


class ParseEnviron:
    headers = {}

    def __init__(self, environ: dict):
        self.environ = environ
        self.headers = {}

    def getRequestHeaders(self):
        for key, value in self.environ.items():
            if key.startswith("HTTP_"):
                header_name = key[5:].replace("_", "-").title()
                self.headers[header_name] = value
            elif key in (
                "CONTENT_TYPE",
                "CONTENT_LENGTH",
                "REQUEST_METHOD",
                "QUERY_STRING",
                "RAW_URI",
                "PATH_INFO",
                "REMOTE_ADDR",
                "Authorization",
            ):
                self.headers[key] = value
        return self.headers

    def getUrl(self):
        return self.environ["PATH_INFO"][
            1:
        ]

    def getPostData(self):
        if "application/json" in self.getContentType():
            return self.extractJsonFromWsgiInput()

        elif "multipart/form-data" in self.getContentType():
            return self.extractFormFromWsgiInput()
        return None

    def getContentLength(self):
        return int(self.headers.get("CONTENT_LENGTH", 0))

    def getContentType(self):
        return self.environ["CONTENT_TYPE"]

    def extractJsonFromWsgiInput(self) -> dict:
        try:
            return json.loads(self.environ["wsgi.input"].read().decode("UTF-8"))
        except:
            return {}

    def extractFormFromWsgiInput(self) -> dict:
        try:
            unparsedData = self.environ["wsgi.input"].read()
            data = pmf(unparsedData).parse()
            return data
        except:
            return {}
