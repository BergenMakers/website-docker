from app import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    #stripeid = db.Column(db.String, unique=True, nullable=False)


    def __init__(self, name=None, email=None, password=None):#, stripeid=None):
        self.name = name
        self.email = email
        self.password = password
        #self.stripeid = stripeid

    def __repr__(self):
        return '<User %r>' % (self.name)