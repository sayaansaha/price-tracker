import os
import httplib2

class PriceFetcher(object):
  """Class for fetching prices from goog api"""
  def __init__(self, arg):
    super(PriceFetcher, self).__init__()
    self.arg = arg
    