from datetime import datetime
from app import db

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        #??? Data is being passed from ???
        #Just prints out this classe's attributes
        return f"Post({self.title}, {self.content})"
