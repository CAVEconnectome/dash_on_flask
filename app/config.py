import os
from dashconnectivityviewer.layout import layout as dcvlayout
from dashconnectivityviewer.callbacks import register_callbacks as dcvregister_callbacks
from dashconnectivityviewer.external_stylesheets import external_stylesheets as dcv_external_stylesheets

class BaseConfig:
    SECRET_KEY = os.environ['SECRET_KEY']
    DASH_DATASTACK_SUPPORT={
        'minnie65_phase3_v1':['connectivity']
    }

    DASH_APPS = {
        'connectivity':{
            'layout': dcvlayout,
            'register_callbacks': dcvregister_callbacks,
            'external_stylesheets': dcv_external_stylesheets,
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