from flask import Flask
from flask import request
from werkzeug.contrib.fixers import ProxyFix
import os

NUM_PROXIES = os.getenv('NUM_PROXIES', '3')
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, num_proxies=int(NUM_PROXIES))

@app.route("/")
def hello():
    ip=request.remote_addr
    return str(request.headers)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
