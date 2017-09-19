import httplib2
import base64

class RestApi(object):
  """docstring for RestApi"""
  def __init__(self, url, api_endpoint):
    self.url = url
    self.api_endpoint = api_endpoint

  def send_get(self, action, first_param=None, **kwargs):
    """"""
    uri = self.format_url(action, first_param, **kwargs)

