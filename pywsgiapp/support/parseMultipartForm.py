import os
import re


class ParseMultipartFormdata:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def parse(self):
        return self.parseMultipartFormdata(self.raw_data)

    def getBoundary(self):
        first_crlf = self.raw_data.find(b'\r\n')
        if first_crlf == -1:
            return None
        boundary_line = self.raw_data[:first_crlf]
        boundary = boundary_line.lstrip(b'-')
        return b'--' + boundary

    def getParts(self):
        full_boundary = self.getBoundary()
        if not full_boundary:
            raise ValueError("Boundary not found in the raw data.")

        parts = self.raw_data.split(full_boundary)
        return parts

    def parseMultipartFormdata(self, raw_data):
        parts = self.getParts()
        result = {}

        for part in parts:
            part = part.strip(b'\r\n')
            if not part or part in (b'--', b'--\r\n'):
                continue

            headersEnd = part.find(b'\r\n\r\n')
            if headersEnd == -1:
                continue
            headersBlock = part[:headersEnd]
            contentBlock = part[headersEnd+4:]

            cdMatch = re.search(
                b'Content-Disposition:\\s*form-data;\\s*(.*)', headersBlock, re.IGNORECASE)
            if not cdMatch:
                continue
            cdData = cdMatch.group(1)

            nameMatch = re.search(b'name="([^"]+)"', cdData)
            filenameMatch = re.search(b'filename="([^"]+)"', cdData)
            if not nameMatch:
                continue

            field_name = nameMatch.group(1).decode('utf-8', 'replace')

            if filenameMatch:
                filename = filenameMatch.group(1).decode('utf-8', 'replace')
                result[field_name] = {
                    'filename': filename,
                    'content': contentBlock
                }
            else:
                result[field_name] = contentBlock.decode('utf-8', 'replace')

        return result
