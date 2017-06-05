import json

from flask import Response
from werkzeug.exceptions import abort


JSON_MIME = 'application/json'


def json_abort(data, status):
    abort(Response(json.dumps(data), mimetype=JSON_MIME, status=status))
