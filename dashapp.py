from app import create_app
# Run a test server.
import os

from werkzeug.serving import WSGIRequestHandler

server = create_app()

if __name__ == "__main__":

    WSGIRequestHandler.protocol_version = "HTTP/1.1"

    server.run(host='0.0.0.0',
                    port=8000,
                    debug=True,
                    threaded=True,
                    ssl_context='adhoc')
