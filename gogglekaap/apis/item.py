from flask import g
from flask_restx import Namespace, Resource, fields, reqparse
from gogglekaap.models.item import Item as ItemModel

# api/item
# docs에 표시되는 URL
ns = Namespace(
    "item",
    description="아이텐 관리 API"
)

# /api/docs  item-GET 항목을 통해서 조회되는 부분
# Models 에 표시되는 사항
item = ns.model("item", {
    "code": fields.String(required=True, description="아이템 코드"),
    "cetegory": fields.String(required=True, description="카테고리"),
    "item_name": fields.String(required=True, description="명칭"),
    "texture": fields.String(required=True, description="재질"),
    "standard_1": fields.String(required=True, description="규격1"),
    "standard_2": fields.String(required=False, description="규격2"),
    "standard_3": fields.String(required=False, description="규격3"),
    "unit": fields.String(required=True, description="단위"),
    "purchase_price": fields.Integer(required=True, description="구매단가"),
    "selling_price": fields.Integer(required=True, description="판매단가"),
    "isMngmnt": fields.Boolean(required=True, description="재고관리여부"),
    "note": fields.String(required=True, description="기타 관리사항"),
    "sort_order": fields.Integer(required=True, description="정렬순서"),
    "created_by": fields.String(required=True, description="최초등록자"),
    "created_at": fields.String(description="최초등록일자")
})

# /api/docs/ 에서 item-POST 항목을 통해 create하는 부분
post_parser = reqparse.RequestParser()
post_parser.add_argument("code", required=True, help="아이템 코드")
post_parser.add_argument("category", required=False, help="카테고리")
post_parser.add_argument("item_name", required=True, help="명칭")
post_parser.add_argument("texture", required=False, help="재질")
post_parser.add_argument("standard_1", required=False, help="규격1")
post_parser.add_argument("standard_2", required=False, help="규격2")
post_parser.add_argument("standard_3", required=False, help="규격3")
post_parser.add_argument("unit", required=False, help="단위")
post_parser.add_argument("purchase_price",type=int, required=False, help="구매단가")
post_parser.add_argument("selling_price", type=int, required=False, help="판매단가")
post_parser.add_argument("isMngmnt", type=bool, required=False, help="재고관리여부")
post_parser.add_argument("note", required=False, help="기타 관리사항")
post_parser.add_argument("sort_order", type=int, required=False, help="정렬순서")
post_parser.add_argument("created_by", required=False, help="최초등록자")

# /api/item
@ns.route("")
class Itemlist(Resource):
    @ns.marshal_list_with(item, skip_none=True)
    def get(self):
        ''' 아이템 조회 '''
        data = ItemModel.query.all()
        return data

    @ns.expect(post_parser)     # 입력 받는 form을 생성
    @ns.marshal_list_with(item, skip_none=True)
    def post(self):
        ''' 아이템 생성 '''
        args = post_parser.parse_args()
        item = ItemModel()
        for key, value in args.items():
            setattr(item, key, value)

        g.db.add(item)
        g.db.commit()
        return item, 201