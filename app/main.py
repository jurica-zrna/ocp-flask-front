import sys
import random
import os
import logging
from flask import Flask, render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)

host = os.getenv('HOSTNAME', 'localhost')
backend_url = os.getenv('BACKEND_URL', 'localhost')
backend_port = os.getenv('BACKEND_PORT', '8080')
title = ("Flask on %s" % host)

@app.route('/')
def index():
    return render_template('index.html', title=title, host=host, url = backend_url, port= backend_port, num = 10)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
