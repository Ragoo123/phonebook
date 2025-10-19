from extensions import db
from flask_login import UserMixin

class Contact(db.Model):
    __tablename__ = "contacts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Contact {self.name} - {self.phone_number}>"