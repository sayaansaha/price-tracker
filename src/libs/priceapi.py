import json

from restapi import RestApi


class PriceFetcher(RestApi):
  """Class for fetching prices from goog api"""
  def __init__(self):
    super(PriceFetcher, self).__init__(
      url='https://www.googleapis.com/qpxExpress/v1/',
      api_endpoint = 'trips')

  def format_url(self, action, first_param=None, data=None):
    """Formats the uri properly"""
    uri = self.url + self.api_endpoint
    uri = uri + '/' + action
    uri = uri + '?key=%s' % self.api_key
    return uri
  
  def date_handler(self, date_string):
    """
    Should handle dates and convert to what is req'd by api.
    @param: date string
    @returns: YYYY-MM-DD
    """    

  def get_price_cancun(self, start_date, return_date):
    """
    Get price for trip to SFO-->CUN
    Should return a price probably
    """
    data = self._create_json_query('SFO', 'CUN', start_date, return_date)
    #https://developers.google.com/qpx-express/v1/requests 
    response = self.send_post('search', first_param=None, data=data)
    if response is not None:
      return response
    else:
      print('Something is up with the response')

  def get_price_cabo(self, start_date, return_date):
    """Get price for trip to SFO-->CABO"""
    data = self._create_json_query('SFO', 'SJD', start_date, return_date)
    #https://developers.google.com/qpx-express/v1/requests 
    response = self.send_post('search', first_param=None, data=data)
    return response

  def _create_json_query(self, origin, destination, start_date, return_date):
    """Returns a json object with specificed request
    Dates are in YYYY-MM-DD"""
    data = {"request":{"passengers":{"adultcount":1},
    "slice":[
    {"origin": str(origin),
    "destination": str(destination),
    "date": str(start_date)
    },{"origin":str(destination),
    "destination":str(origin),
    "date":str(return_date)
    }]}}
    json_data = json.dumps(data)
    return json_data