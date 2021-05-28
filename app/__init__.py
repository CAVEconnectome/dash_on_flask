import dash
from flask import Flask
from flask.helpers import get_root_path
from middle_auth_client import (auth_required, auth_requires_admin,
                                auth_requires_permission)
from .config import configure_app
import os

def create_app():
    server = Flask(__name__, static_folder='./static',
                   static_url_path='/dash/static',
                   instance_relative_config=True)
    server=configure_app(server)

    register_dashapps(server)
    register_extensions(server)
    register_blueprints(server)

    return server

def register_dashapps(app):
    
    # Meta tags for viewport responsiveness
    meta_viewport = {"name": "viewport",
                     "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}
    dashapps =[]
    for dapp,dapp_config in app.config['DASH_APPS'].items():
            
        dashapp1 = dash.Dash(__name__ + dapp,
                            server=app,
                            url_base_pathname=f'/dash/apps/{dapp}/',
                            assets_folder=get_root_path(__name__) + f'/{dapp}/apps/assets/',
                            external_stylesheets=dapp_config.get('external_stylesheets', None),
                            meta_tags=[meta_viewport])

        with app.app_context():
            dashapp1.title = dapp
            dashapp1.layout = dapp_config['layout']
            dapp_config['register_callbacks'](dashapp1, dapp_config['config'])

        _protect_dashviews(dashapp1)
        dashapps.append(dashapp1)


def _protect_dashviews(dashapp):
    for view_func in dashapp.server.view_functions:
        if view_func.startswith(dashapp.config.url_base_pathname):
            #todo: add middle auth client protection here
            dashapp.server.view_functions[view_func] = auth_required(func=dashapp.server.view_functions[view_func])


def register_extensions(server):
    pass


def register_blueprints(server):
    from app.webapp import server_bp

    server.register_blueprint(server_bp,
                              url_prefix='/dash/')
