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
    # show a list of datastacks in config
    return render_template("index.html", title='Home Page', version=__version__)

@server_bp.route('/datastack/<datastack_name>')
def datastack_view(datastack_name):
    #show me a page with all apps supported by datastack
    return render_template("datastack.html",
                           datastack=datastack_name,
                           title='Home Page',
                           version=__version__)

