import os
import json
from flask import Blueprint, send_from_directory, render_template


def get_swaggerui_blueprint(base_url, api_url, config=None):

    swagger_ui = Blueprint('swagger_ui',
                           __name__,
                           static_folder='dist',
                           template_folder='templates')

    default_config = {
        'client_realm': 'null',
        'client_id': 'null',
        'client_secret': 'null',
        'app_name': 'null',
        'docExpansion': "none",
        'jsonEditor': False,
        'defaultModelRendering': 'schema',
        'showRequestHeaders': False,
        'supportedSubmitMethods': ['get', 'post', 'put', 'delete', 'patch']
    }

    if config:
        default_config.update(config)

    fields = {
        # Some fields are used in functions etc, so we treat them special
        'base_url': base_url,
        'api_url': api_url,
        'app_name': default_config.pop('app_name'),
        'client_realm': default_config.pop('client_realm'),
        'client_id': default_config.pop('client_id'),
        'client_secret': default_config.pop('client_secret'),

        # Rest are just serialized into json string for inclusion in the .js file
        'config_json': json.dumps(default_config)
    }

    @swagger_ui.route('/')
    @swagger_ui.route('/<path:path>')
    def show(path=None):
        if not path or path == 'index.html':
            return render_template('index.template.html', **fields)
        else:
            return send_from_directory(
                # A bit of a hack to not pollute the default /static path with our files.
                os.path.join(
                    swagger_ui.root_path,
                    swagger_ui._static_folder
                ),
                path
            )

    return swagger_ui
