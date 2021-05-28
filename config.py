import os
from dashconnectivityviewer.layout import layout as dcvlayout
from dashconnectivityviewer.callbacks import register_callbacks as dcvregister_callbacks

class BaseConfig:
    SECRET_KEY = os.environ['SECRET_KEY']
    DASH_DATASTACK_SUPPORT={
        'minnie65_phase3_v1':['connectivity']
    }

    DASH_APPS = {
        'connectivity':{
            'layout': dcvlayout,
            'register_callbacks': dcvregister_callbacks,
            'config': {}
        }
    }