from flask_restplus import Resource, reqparse, abort
from response import Response


class ApiRoute(object):
	"""docstring for ApiRoute"""
	def __init__(self):
		super(ApiRoute, self).__init__()


	def get(self):
		"""
		Class to handle basic routing and response handles.
		"""
