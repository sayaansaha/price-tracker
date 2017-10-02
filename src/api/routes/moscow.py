from ..route import ApiRoute

class Moscow(ApiRoute):
  """docstring for Moscow"""
  def __init__(self, arg):
    super(Moscow, self).__init__()

  def format_uri(self):
    """
    format the uri for proper passing 
    to price tracker.
    """
    pass

  def get(self):
    """return price for trip"""
    pass