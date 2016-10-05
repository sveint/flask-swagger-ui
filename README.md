# flask-swagger-ui

Simple Flask blueprint for adding [Swagger UI](https://github.com/swagger-api/swagger-ui) to your flask application.

Included Swagger UI version: 2.2.5.

## Installation

`pip install flask-swagger-ui`

## Usage

Example application:

```python
from flask import Flask
from swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)


SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'http://petstore.swagger.io/v2/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'supportedSubmitMethods': ['get']
    }
)

# Register blueprint at URL
# (URL must match the one given to factory function above)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

app.run()

# Now point your browser to localhost:5000/api/docs/

```

## Configuration

The blueprint supports overloading all Swagger UI configuration options that can be JSON serialized.
See https://github.com/swagger-api/swagger-ui#parameters for options.

In addition, some of the OAuth fields are exposed to special variables that will be rendered into the relevant function.

Blueprint defaults are listed below (should match SwaggerUI defaults).

```python
{
        # OAuth related
        'app_name': 'null',
        'client_realm': 'null',
        'client_id': 'null',
        'client_secret': 'null',

        # SwaggerUI base configuration, see https://github.com/swagger-api/swagger-ui#parameters
        'docExpansion': "none",
        'jsonEditor': False,
        'defaultModelRendering': 'schema',
        'showRequestHeaders': False,
        'supportedSubmitMethods': ['get', 'post', 'put', 'delete', 'patch']
}
```
