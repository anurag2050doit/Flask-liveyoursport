from liveyoursport import db

class User(db.Model):
    id = db.Column('user_id', db.Integer, primary_key=True)
    full_name = db.Column(db.String(90))
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    email = db.Column(db.String(35), unique=True)
    username = db.Column(db.String(60),unique=True)
    password = db.Column(db.String(60))


    def __init__(self,full_name,first_name,last_name,email,username,password):
        self.full_name = full_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return '<Full Name %r>' % self.full_name
