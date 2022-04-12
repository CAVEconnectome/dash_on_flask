import os
from dash_connectivity_viewer import (
    cell_type_connectivity,
    cell_type_table,
    connectivity_table,
)
import json

ct_config = {
    "cell_type_dropdown_options": [
        {
            "label": "All Soma Prediction",
            "value": "allen_soma_coarse_cell_class_model_v1",
        },
        {
            "label": "Column Census (slanted)",
            "value": "allen_v1_column_types_slanted",
        },
        {
            "label": "Column Census (straight)",
            "value": "allen_v1_column_types_v2",
        },
        {
            "label": "Thalamic Axons",
            "value": "allen_v1_column_thalamic",
        },
        {
            "label": "Layer 5 IT PyC Subtypes",
            "value": "allen_column_l5it_types",
        },
        {
            "label": "Basket Subtypes",
            "value": "allen_column_basket_molecular",
        },
    ],
    "omit_cell_type_tables": ["nucleus_neuron_svm"],
    "valence_map_table": {
        "allen_v1_column_types_slanted": [
            "classification_system",
            "aibs_coarse_excitatory",
            "aibs_coarse_inhibitory",
        ],
        "allen_soma_coarse_cell_class_model_v1": [
            "classification_system",
            "aibs_coarse_excitatory",
            "aibs_coarse_inhibitory",
        ],
    },
    "cell_type_column_schema_lookup": {
        "cell_type_local": "cell_type",
    },
}


class BaseConfig:

    daf_credential_path = os.environ.get("DAF_CREDENTIALS", None)
    if daf_credential_path is not None:
        with open(daf_credential_path, "r") as f:
            AUTH_TOKEN = json.load(f)["token"]
    else:
        AUTH_TOKEN = ""
    SECRET_KEY = os.environ["SECRET_KEY"]
    DASH_DATASTACK_SUPPORT = {
        "minnie65_phase3_v1": {
            "cell_type": {
                "create_app": cell_type_table.create_app,
                "config": ct_config,
            },
            "connectivity": {
                "create_app": cell_type_connectivity.create_app,
                "config": ct_config,
            },
            "basic_connectivity": {
                "create_app": connectivity_table.create_app,
                "config": {},
            },
        },
        "minnie65_public_v117": {
            "cell_type": {
                "create_app": cell_type_table.create_app,
                "config": ct_config,
            },
            "connectivity_table": {
                "create_app": connectivity_table.create_app,
                "config": {},
            },
        },
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
