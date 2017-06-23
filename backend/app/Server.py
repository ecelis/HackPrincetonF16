import os
import logging
from flask import Flask, request
from flask_cors import CORS, cross_origin
from imageverify import main

logging.getLogger('flask-cors').level = logging.DEBUG

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
@cross_origin(allow_headers=['Content-Type'])
def hello():
    user = request.args.get('content')
    # Workaround a weird value sent from browser extension
    status = main(user)
    return status

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port, ssl_context=('cert.pem', 'key.pem'))
