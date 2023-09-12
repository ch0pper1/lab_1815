from flask import Flask, jsonify, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Serve the OpenAPI JSON specification
@app.route('/openapi.json')
def serve_openapi_spec():
    with open('openapi.json', 'r') as spec_file:
        spec_content = spec_file.read()
        return jsonify(spec_content)

# Serve the Swagger UI for visualizing the OpenAPI specification
SWAGGER_URL = '/swagger'
API_URL = '/openapi.json'
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "My Awesome API"
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Serve static files (for Swagger UI)
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)

