from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<Player {} {}>'.format(self.first_name, self.last_name)

