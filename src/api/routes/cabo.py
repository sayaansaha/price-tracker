from ..route import ApiRoute

class Cabo(ApiRoute):
  """docstring for Cabo"""
  def __init__(self, arg):
    super(Cabo, self).__init__()

  def format_uri(self):
    """
    format the uri for proper passing 
    to price tracker.
    """
    pass

  def get(self):
    """return price for trip"""
    try:
      data = self.price_fetcher.get_price_cabo
    except Exception as e:
      raise e