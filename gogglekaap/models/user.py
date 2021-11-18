from gogglekaap import db
from sqlalchemy import func

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(20), unique=True, nullable=False)
    user_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime(), server_default=func.now())
    # server_default=func.now() 기존에 데이터들의 빈 자리도 채워줌
    # default=func.now() 새로 migration을 한 이후에 생성된 데이터에 대해서만 적용

    @classmethod
    def find_one_by_user_id(cls, user_id):
        return User.query.filter_by(user_id=user_id).first()