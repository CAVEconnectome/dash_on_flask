from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for


from werkzeug.urls import url_parse

__version__ = "0.0.1"

server_bp = Blueprint('main', __name__)


@server_bp.route('/')
def index():
    return render_template("index.html", title='Home Page', version=__version__)

