from flask_restplus import Resource, reqparse, abort
from response import Response
from lib.priecapi import PriceFetcher


class ApiRoute(Resource):
  """docstring for ApiRoute"""
  def __init__(self):
    super(ApiRoute, self).__init__()
    _base_uri = "/api/v1.0/"
    has_id_args = False
    price_fetcher = PriceFetcher()

  def uri(cls):
    """
    Overload this if required in other classes.
    """
    return ApiRoute._base_uri + cls.__name__.lower()

  def get(self):
    """
    Class to handle basic routing and response handles.
    """
    try:
      if self.has_id_args:
        parser = reqparse.RequestParser()

    except Exception as e:
      raise e

