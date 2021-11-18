from flask_restx import Api
from flask import Blueprint
from .user import ns as UserNamespace
from .item import ns as ItemNamespace


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
    description="Welcome my api docs"
)


# TODO: add namespace to Blueprint
api.add_namespace(UserNamespace)
api.add_namespace(ItemNamespace)