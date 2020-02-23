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
url = os.getenv('BACKEND_URL', 'localhost')
title = ("Flask on %s" % host)

@app.route('/')
def index():
    return render_template('index.html', title=title, host=host, url = url, num = 10)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
