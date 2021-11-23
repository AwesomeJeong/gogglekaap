from flask import g
from flask_restx import Namespace, Resource, fields, reqparse
from gogglekaap.models.partner import Partner as PartnerModel

ns = Namespace(
    "partners",
    description="거래처 API"
)
'''
    code = db.Column(db.Integer, primary_key=True)
    co_name = db.Column(db.String(20))
    business_type = db.Column(db.String(20), nullable=True)
    co_type = db.Column(db.String(20), nullable=True)
    repre = db.Column(db.String(20))
    business_no = db.Column(db.String(20))
    person = db.Column(db.String(20), nullable=True)
    contact = db.Column(db.String(20))
    cellphone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(20))
    address1 = db.Column(db.String(20))
    address2 = db.Column(db.String(20), nullable=True)
    note = db.Column(db.String(20), nullable=True)
    created_by = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime(), default=func.now())
'''
# partner 조회
partner = ns.model("partner", {
    "code": fields.Integer(required=True, description="거래처 코드"),
    "co_name": fields.String(required=True, description="거래처명"),
    "business_type": fields.String(required=False, description="거래유형"),
    "co_type": fields.String(required=False, description="사업자종류"),
    "repre": fields.String(required=False, description="대표자"),
    "business_no": fields.String(required=False, description="사업자번호"),
    "person": fields.String(required=False, description="담당자"),
    "contact": fields.String(required=False, description="연락처"),
    "cellphone": fields.String(required=False, description="휴대폰"),
    "email": fields.String(required=False, description="이메일"),
    "address1": fields.String(required=False, description="주소"),
    "address2": fields.String(required=False, description="상세주소"),
    "note": fields.String(required=False, description="비고"),
    "created_by": fields.String(required=False, description="최초등록자"),
    "created_at": fields.String(description="최초등록일자")
})

# partner 입력
post_parser = reqparse.RequestParser()
post_parser.add_argument("code", type=int, required=True, help="거래처명 코드")
post_parser.add_argument("co_name", required=True, help="거래처명")
post_parser.add_argument("business_type", required=False, help="거래유형")
post_parser.add_argument("co_type", required=False, help="사업자종류")
post_parser.add_argument("repre", required=False, help="대표자")
post_parser.add_argument("business_no", required=False, help="사업자번호")
post_parser.add_argument("person", required=False, help="담당자")
post_parser.add_argument("contact", required=False, help="연락처")
post_parser.add_argument("cellphone", required=False, help="휴대폰")
post_parser.add_argument("email", required=False, help="이메일")
post_parser.add_argument("address1", required=False, help="주소")
post_parser.add_argument("address2", required=False, help="상세주소")
post_parser.add_argument("note", required=False, help="비고")
post_parser.add_argument("created_by", required=False, help="최초등록자")

@ns.route("")
class PartnerList(Resource):
    @ns.marshal_list_with(partner, skip_none=True)
    def get(self):
        ''' 거래처 복수 조회 '''
        data = PartnerModel.query.all()
        return data
    
    @ns.expect(post_parser)
    @ns.marshal_list_with(partner, skip_none=True)
    def post(self):
        ''' 거래처 생성 '''
        args = post_parser.parse_args()
        partner = PartnerModel()
        for key, value in args.items() :
            setattr(partner, key, value)

        g.db.add(partner)
        g.db.commit()
        return partner, 201