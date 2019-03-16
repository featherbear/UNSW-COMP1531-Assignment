# Utility functions go here
# ... if there even are any

import json

def createResponse(status, obj = {}, **kwargs):
  resp = dict(status = status)
  resp.update(obj)
  resp.update(kwargs)
  return resp

def createJSON(status, obj = {}, **kwargs):
  return json.dumps(createResponse(status, obj, **kwargs))
