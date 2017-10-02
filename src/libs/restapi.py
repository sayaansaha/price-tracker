import urllib2
import base64
import os
import json

class RestApi(object):
  """docstring for RestApi"""
  def __init__(self, url, api_endpoint, api_key):
    self.url = url
    self.api_endpoint = api_endpoint
    self.api_key = api_key 

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
    return self._send_request(method='POST', uri=uri, data=None)

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
    url = self.api_endpoint + uri
    request = urllib2.Request(url)
    if method == 'POST':
      request.add_data(json.dumps(data))
    request.add_header('Content-Type', 'application/json')
    request.add_header('User-Agent', 'price-tracker')
    try:
      response = urllib2.urlopen(request).read()
    except urllib2.HTTPError as e:
      response = e.read()
    if response:
      result = json.loads(response)
    else:
      result = {}
    return result
  
  def format_url(self, action, first_param=None):
    """
    Formats the string we append to our URL for API calls.
    Necessary, because some API calls treat the first parameter as an end point in the url rather
    than a url parameter.

    :param action: String representing the API action we want to do.
    :param end_point: The end point variable (if there is one).
    :param kwargs: Additional url parameters that we want to attach to our API call.

    :type action: str
    :type end_point: str
    :type kwargs: dict
    :rtype: str
    """
    uri = action + '/'
    if self.api_endpoint is not None:
      uri = uri + self.api_endpoint
    return uri
    

