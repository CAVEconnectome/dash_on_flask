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