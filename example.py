from flask import Flask, url_for
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config['SERVER_NAME'] = "127.0.0.1:5000"


SWAGGER_URL = "/api/docs"  # URL for exposing Swagger UI (without trailing '/')
API_URL = (
    "http://petstore.swagger.io/v2/swagger.json"
)  # Our API url (can of course be a local resource)

with app.app_context():
    icons = [{
        "href": url_for("static", filename="favicon.ico"),
        "sizes": "32x32" # optional key
    }]

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={"app_name": "Test application"},  # Swagger UI config overrides
    # oauth_config={  # OAuth config. See swagger-ui docs.
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
    # icons=icons
)

app.register_blueprint(swaggerui_blueprint)

app.run(host="127.0.0.1")

# Now point your browser to localhost:5000/api/docs/
