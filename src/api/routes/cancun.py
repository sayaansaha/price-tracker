from ..route import ApiRoute

class Cancun(ApiRoute):
  """docstring for Cacun"""
  def __init__(self, arg):
    super(Cancun, self).__init__()

  def format_uri(self):
    """
    format the uri for proper passing 
    to price tracker.
    """
    pass

  def get(self):
    """return price for trip"""
    pass