from rest_framework import parsers
import json


class CustomMultipartParser(parsers.MultiPartParser):

    def decode(self, key, value, data):
        if key in ['skills', 'languages']:
            data[key] = json.loads(value)
        else:
            data[key] = value

    def parse(self, stream, media_type=None, parser_context=None):
        result = super().parse(stream=stream, media_type=media_type, parser_context=parser_context)
        data = {}

        for key, value in result.data.items():
            self.decode(key=key, value=value, data=data)

        for key, value in result.files.items():
            self.decode(key=key, value=value, data=data)

        return data
