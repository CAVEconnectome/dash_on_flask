from flask import Blueprint
from flask import render_template
from middle_auth_client import auth_requires_permission

__version__ = "1.8.0"

server_bp = Blueprint("main", __name__)


@server_bp.route("/")
def index():
    # show a list of datastacks in config
    return render_template("index.html", title="Home Page", version=__version__)


@server_bp.route("/datastack/<datastack_name>")
@auth_requires_permission(
    "view", table_arg="datastack_name", resource_namespace="datastack"
)
def datastack_view(datastack_name):
    # show me a page with all apps supported by datastack
    return render_template(
        "datastack.html",
        datastack=datastack_name,
        title="Home Page",
        version=__version__,
    )
