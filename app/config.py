import os
from dashconnectivityviewer import create_app
from dashcelltypeviewer import create_app as celltype_create_app

class BaseConfig:
    SECRET_KEY = os.environ['SECRET_KEY']
    DASH_DATASTACK_SUPPORT={
        'minnie65_phase3_v1':['connectivity', 'cell_type'],
    }

    DASH_APPS = {
        'connectivity':{
            'create_app': create_app,
            'config': {}
        },
        'cell_type':{
            'create_app': celltype_create_app,
            'config': {}
        }
    }

config = {
    "default": "app.config.BaseConfig",
    "development": "app.config.BaseConfig",
    "testing": "app.config.BaseConfig",
    "production": "app.config.BaseConfig",
}

def configure_app(app):
    config_name = os.getenv("FLASK_CONFIGURATION", "default")
    # object-based default configuration
    app.config.from_object(config[config_name])
    if "DASH_SETTINGS" in os.environ.keys():
        app.config.from_envvar("DASH_SETTINGS")
    # instance-folders configuration
    app.config.from_pyfile("config.cfg", silent=True)
    return app