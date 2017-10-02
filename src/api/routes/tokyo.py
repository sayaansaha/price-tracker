from ..route import ApiRoute

class Tokyo(ApiRoute):
  """docstring for Tokyo"""
  def __init__(self, arg):
    super(Tokyo, self).__init__()

  def format_uri(self):
    """
    format the uri for proper passing 
    to price tracker.
    """
    pass

  def get(self):
    """return price for trip"""
    pass