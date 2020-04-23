from flask import Blueprint

hello_routes = Blueprint("hello_routes", __name__)

@hello_routes.route("/")
@hello_routes.route("/home")
def hello_world():
    return "Hello World!"