#!/usr/bin/python3
"""
starts the  Flask api app.
"""

from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
cors = CORS(app, origins='0.0.0.0')
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """close the storage on the teardown"""
    storage.close()


@app.errorhandler(404)
def endpoint_not_found(error):
    """Handle not found404 err."""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    """Starts Point of the app"""
    host = getenv("HBNB_API_HOST")
    if not host:
        host = '0.0.0.0'
    port = getenv("HBNB_API_PORT")
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
