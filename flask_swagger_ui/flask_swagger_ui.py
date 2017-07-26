import os
import json
from flask import Blueprint, send_from_directory, render_template


def get_swaggerui_blueprint(base_url, api_url, config=None, oauth_config=None):

    swagger_ui = Blueprint('swagger_ui',
                           __name__,
                           static_folder='dist',
                           template_folder='templates')

    default_config = {
        'app_name': 'Swagger UI',
        'dom_id': '#swagger-ui',
        'url': api_url,
        'layout': 'StandaloneLayout'
    }

    if config:
        default_config.update(config)

    fields = {
        # Some fields are used directly in template
        'base_url': base_url,
        'cdn_url': 'https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.0.17',
        'app_name': default_config.pop('app_name'),
        # Rest are just serialized into json string for inclusion in the .js file
        'config_json': json.dumps(default_config),

    }
    if oauth_config:
        fields['oauth_config_json'] = json.dumps(oauth_config)

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
