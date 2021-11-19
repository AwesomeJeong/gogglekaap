from gogglekaap import db
from sqlalchemy import func

class Partner(db.Model):
    code = db.Column(db.Integer, primary_key=True)
    co_name = db.Column(db.String(20), nullable=False)
    business_type = db.Column(db.String(20))
    co_type = db.Column(db.String(20))
    repre = db.Column(db.String(20))
    business_no = db.Column(db.String(20))
    person = db.Column(db.String(20))
    contact = db.Column(db.String(20))
    cellphone = db.Column(db.String(20))
    email = db.Column(db.String(20))
    address1 = db.Column(db.String(20))
    address2 = db.Column(db.String(20))
    note = db.Column(db.String(20))
    created_by = db.Column(db.String(20))
    created_at = db.Column(db.DateTime(), default=func.now())
