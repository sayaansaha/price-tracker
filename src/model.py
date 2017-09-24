from app import db
from sqlalchemy.dialects.postgresql import JSON

class FlightPrice(db.Model):
  __tablename__ = 'prices'

  id = db.Column(db.Integer, primary_key=True)
  destination = db.Column(db.String())
  price = db.Column(db.Float)
  flight_time = Column(db.DateTime)
  start_date = Column(db.DateTime)
  return_date = Column(db.DateTime)


  def __init__(self, destination, flight_time, price, start_date, return_date):
    self.destination = destination
    self.flight_time = flight_time
    self.price = price
    self.start_date = start_date
    self.return_date = return_date

  def __repr__(self):
    return '<id {}>'.format(self.id
