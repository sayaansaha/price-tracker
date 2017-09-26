from flask import Flask
import os
from flask.ext.sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from model import FlightPrices

@app.route('/')
def hello():
	return 'Hello Worldz'

@app.route('/<name>')
def hello_name(name):
  return "Hello {}!".format(name)
@app.route('/readme')
def readme_page(name):
	return 'Go readme'


if __name__ == '__main__':
  app.run()