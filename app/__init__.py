import dash
from flask import Flask
from flask.helpers import get_root_path
from middle_auth_client import (
    auth_required,
    auth_requires_admin,
    auth_requires_permission,
)
from .config import configure_app
from .reset_auth import reset_auth
import os


def create_app():
    server = Flask(
        __name__,
        static_folder="./static",
        static_url_path="/dash/static",
        instance_relative_config=True,
    )
    server = configure_app(server)

    register_dashapps(server)
    register_extensions(server)
    register_blueprints(server)

    return server


def register_dashapps(app):

    # Meta tags for viewport responsiveness
    meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no",
    }
    dashapps = []
    for datastack, dapps in app.config["DASH_DATASTACK_SUPPORT"].items():
        for dapp, dapp_config in dapps.items():
            create_app = dapp_config["create_app"]
            with app.app_context():
                dashapp1 = create_app(
                    __name__ + dapp,
                    config=dapp_config["config"],
                    server=app,
                    url_base_pathname=f"/dash/datastack/{datastack}/apps/{dapp}/",
                    assets_folder=get_root_path(__name__)
                    + f"/dash/datastack/{datastack}/apps/{dapp}/",
                    meta_tags=[meta_viewport],
                )

            _protect_dashviews(dashapp1, datastack)
            dashapps.append(dashapp1)


def _protect_dashviews(dashapp, datastack):
    for view_func in dashapp.server.view_functions:
        if view_func.startswith(dashapp.config.url_base_pathname):
            # todo: add middle auth client protection here
            print("protecting", view_func)
            dashapp.server.view_functions[view_func] = auth_requires_permission(
                "view", table_id=datastack, resource_namespace="datastack"
            )(dashapp.server.view_functions[view_func])


def register_extensions(server):
    pass


def register_blueprints(server):
    from app.webapp import server_bp

    server.register_blueprint(server_bp, url_prefix="/dash/")
