from liveyoursport import db
from datetime import datetime

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(20))
    product_name = db.Column(db.String(200))
    order_status = db.Column(db.String(10))
    product_url = db.Column(db.String(150))
    cost_price = db.Column(db.Float)
    order_date = db.Column(db.DateTime)

    def __init__(self,order_id,product_name,order_status,product_url,cost_price,order_date):
        self.order_id = order_id
        self.product_name = product_name
        self.order_status = order_status
        self.product_url = product_url
        self.cost_price = cost_price
        self.order_date = order_date
        self.order_date = order_date

    def __repr__(self):
        return '<order_id %r>' % self.order_id
