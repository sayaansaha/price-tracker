import urllib2
import base64
import os
import json
from config import Config

class RestApi(object):
  """docstring for RestApi"""
  def __init__(self, url, api_endpoint):
    self.url = url
    self.api_endpoint = api_endpoint
    self.api_key = Config.api_key 

  def send_get(self, action, first_param=None):
    """
    Issues a GET request (read) against the API and returns the result.

    :param action: The API method to call.
    :param first_param: First parameter we want to include if we need to.
    :param kwargs: other parameters to include in our request.
    :return: Response from the server (if we got one).

    :type action: str
    :type kwargs: dict
    :return type: dict
    """
    uri = self.format_url(action, first_param)
    print(uri)
    return self._send_request(method='GET', uri=uri)

  def send_post(self, action, first_param=None, data=None):
    """
    Issues a Post request (read) against the API and returns the result.

    :param action: The API method to call.
    :param first_param: First parameter we want to include if we need to.
    :param kwargs: other parameters to include in our request.
    :return: Response from the server (if we got one).

    :type action: str
    :type kwargs: dict
    :return type: dict
    """
    uri = self.format_url(action, first_param)
    print(uri)
    return self._send_request(method='POST', uri=uri, data=data)

  def _send_request(self, method, uri, data=None):
    """
    Issues a request to our Confluence API and returns the json response we got back.

    :param method: Either 'POST' or 'GET'.
    :param uri: The actual URL arguments for our request that we'll send up.
    :param data: In the event of a post, we'll send this data with our request.
    :return: Response from the server (if we got one).

    :type method: str
    :type uri: str
    :type data: dict
    :return type: dict
    """
    url = uri + self.api_endpoint
    request = urllib2.Request(url)
    if method == 'POST':
      print(data)
      request.add_data(json.dumps(data))
    request.add_header('Content-Type', 'application/json')
    request.add_header('User-Agent', 'price-tracker')
    #TODO(Sayaan): Add Auth to header
    try:
      response = urllib2.urlopen(request).read()
    except urllib2.HTTPError as e:
      response = e.read()
    if response:
      print(response)
      return response
      #result = json.loads(response)
    else:
      result = {}
    return result

  def format_url(self, action, first_param=None):
    """Formats the uri properly"""
    uri = self.url + self.api_endpoint
    uri = uri + '/' + action
    return uri
    

