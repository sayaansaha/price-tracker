import os
import httplib2
import json
import datetime
from restapi import RestApi
from congig import Config
class PriceFetcher(RestApi):
  """Class for fetching prices from goog api"""
  def __init__(self, arg):
    super(PriceFetcher, self).__init__(
      url='https://www.googleapis.com/qpxExpress/v1/',
      api_endpoint = 'trips',
      api_key=Config.api_key)
    self.arg = arg
  
  def get_price_cuncun(self, start_date, return_date):
    """Should return a price probably"""
    data = #json type data like in 
    #https://developers.google.com/qpx-express/v1/requests 
    response = self.send_post('search', first_param=None, data=data)

  def get_price_cabo(self, start_date, return_date):
    """Get price for trip to SFO-->CABO"""
    data = #json type data like in 
    #https://developers.google.com/qpx-express/v1/requests 
    response = self.send_post('search', first_param=None, data=data)

  def _create_json_query(self, origin, destination, start_date, return_date):
    """Returns a json object with specificed request"""
    data = {"request":{"passengers":{"adultcount":1},
    "slice":[
    {"origin":str(origin),
    "destination":str(destination),
    "date":str(start_date)
    },{"origin":str(destination),
    "destination":str(origin),
    "date":str(return_date)
    }]}}
    json_data = json.dumps(data)
    return json_data