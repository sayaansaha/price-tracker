from flask.ext.restful import Resource, reqparse, abort

class DataPrices(Resource):
	"""docstring for DataPrices"""
	def __init__(self):
		super(DataPrices, self).__init__()
		self.arg = arg

	def get(self):
		"""
		Called when the user hits the tables
		endpoint looking for the table dump.
		"""
		