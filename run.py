from flask import Flask
from flask import request
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, num_proxies=2)

@app.route("/")
def hello():
    ip=request.remote_addr
    print(ip)
    return ip

if __name__ == "__main__":
    app.run(host='0.0.0.0')
