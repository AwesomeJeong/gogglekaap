from flask_restx import Api
from flask import Blueprint, g, abort
from .user import ns as UserNamespace
from .item import ns as ItemNamespace
from .parter import ns as PartnerNamespace
from functools import wraps

# 데코레이션 패턴 공부하면 알게 될 내용인데 개인적으로 공부해보면 좋을 듯
def check_session(func):
    @wraps(func)
    def __wrapper(*args, **kwargs):
        if not g.user:
            abort(401)
        return func(*args, **kwargs)
    return __wrapper

blueprint = Blueprint(
    "api",
    __name__,
    url_prefix="/api"
)

api = Api(
    blueprint,
    title="gogglekapp API",
    version="1.0",
    doc="/docs",
    decorators=[check_session],
    description="Welcome my api docs"
)


# TODO: add namespace to Blueprint
api.add_namespace(UserNamespace)
api.add_namespace(ItemNamespace)
api.add_namespace(PartnerNamespace)