from flask import Blueprint
from flask import render_template

errors = Blueprint("errors", __name__)


@errors.errorhandler(500)
def internal_server_error():
    return render_template("errors/500.jinja"), 500
    

@errors.errorhandler(400)
def internal_server_error():
    return render_template("errors/400.jinja"), 400

