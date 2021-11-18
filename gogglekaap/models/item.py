from gogglekaap import db
from sqlalchemy import func

class Item(db.Model):
    code = db.Column(db.String(20), primary_key=True)
    category = db.Column(db.String(20), nullable=True)
    item_name = db.Column(db.String(20), nullable=False)
    texture = db.Column(db.String(20), nullable=True)
    standard_1 = db.Column(db.String(20), nullable=True)
    standard_2 = db.Column(db.String(20), nullable=True)
    standard_3 = db.Column(db.String(20), nullable=True)
    unit = db.Column(db.String(20), nullable=True)
    purchase_price = db.Column(db.Integer, nullable=True)
    selling_price = db.Column(db.Integer, nullable=True)
    isMngmnt = db.Column(db.Boolean, nullable=True)
    note = db.Column(db.String(20), nullable=True)
    sort_order = db.Column(db.Integer, nullable=True)
    created_by = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime(), default=func.now())
