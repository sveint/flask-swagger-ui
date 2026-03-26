import json
import os
from flask import Blueprint, send_from_directory, render_template, request

_DIST_DIR = os.path.join(os.path.dirname(__file__), "dist")


def get_swaggerui_blueprint(
    base_url, api_url, config=None, oauth_config=None, blueprint_name="swagger_ui"
):

    swagger_ui = Blueprint(
        blueprint_name,
        __name__,
        template_folder="templates",
        url_prefix=base_url,
    )

    default_config = {
        "app_name": "Swagger UI",
        "dom_id": "#swagger-ui",
        "url": api_url,
        "layout": "StandaloneLayout",
        "deepLinking": True,
    }

    if config:
        default_config.update(config)

    app_name = default_config.pop("app_name")

    oauth_fields = {}
    if oauth_config:
        oauth_fields["oauth_config_json"] = json.dumps(oauth_config)

    @swagger_ui.route("/")
    @swagger_ui.route("/<path:path>")
    def show(path=None):
        if not path or path == "index.html":
            request_config = dict(default_config)
            if "oauth2RedirectUrl" not in request_config:
                request_config["oauth2RedirectUrl"] = (
                    request.base_url.rstrip("/") + "/oauth2-redirect.html"
                )
            return render_template(
                "index.template.html",
                base_url=base_url,
                app_name=app_name,
                config_json=json.dumps(request_config),
                **oauth_fields,
            )
        else:
            return send_from_directory(_DIST_DIR, path)

    return swagger_ui
