import sys
import random
import os
import logging
from flask import Flask, render_template, make_response
app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

host = os.getenv('HOSTNAME', 'localhost')
backend_url = os.getenv('BACKEND_URL', 'localhost')
backend_port = os.getenv('BACKEND_PORT', '8080')
title = ("Flask on %s" % host)

@app.route('/')
def index():
    response = make_response(render_template('index.html', title=title, host=host, url = backend_url, port= backend_port, num = 10))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
