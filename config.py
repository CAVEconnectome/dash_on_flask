import os
from dashconnectivityviewer.layout import layout as dclayout
import dashconnectivityviewer.callbacks

class BaseConfig:
    SECRET_KEY = os.environ['SECRET_KEY']

    DASH_APPS = {
        'connectivity':{
            'layout': dclayout,
            'register_callbacks': dashconnectivityviewer.callbacks.register_callbacks,
            'config': {}
        }
    }