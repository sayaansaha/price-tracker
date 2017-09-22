import urllib2
import base64
import os
import json

class RestApi(object):
  """docstring for RestApi"""
  def __init__(self, url, api_endpoint):
    self.url = url
    self.api_endpoint = api_endpoint

  def send_get(self, action, first_param=None, **kwargs):
    """Sends a GET request"""
    uri = self.format_url(action, first_param, **kwargs)

  def _send_request(self, method, uri, data=None):
  	url = self.api_endpoint + uri
  	request = urllib2.Request(url)
  	if method == 'POST':
  		request.add_data(json.dumps(data))
  	request.add_header('Content-Type', 'application/json')
  	request.add_header('User-Agent', 'lossless-app')
  	try:
  		response = urllib2.urlopen(request).read()
  	except urllib2.HTTPError as e:
  		response = e.read()
  	if response:
  		result = json.loads(response)
  	else:
  		result = {}
  	return result
  	

