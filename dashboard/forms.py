from flask_wtf import Form
from wtforms import StringField, validators, PasswordField, SelectField, IntegerField

class OrderForm(Form):
    order_id = StringField('Order ID', [validators.Required()])
    order_status = SelectField('Order Status ', choices=[("Active","Active"),("Cancelled","Cancelled")],[validators.Required()])
    product_name = StringField('Product Name ', [validators.DataRequired()])
	product_url	 = StringField('Product Url ', [
        validators.Required(),
    ])
    cost_price = IntegerField('Cost Price', [
        validators.Required(),
    ])
