from flask import Flask, render_template
from pykube import Deployment, HTTPClient, KubeConfig

api = HTTPClient(KubeConfig.from_file('~/.kube/config'))

app = Flask(__name__)


@app.route('/')
def home():
    deployments = Deployment.objects(api).filter(namespace='default')
    return render_template('home.html', deployments=deployments)
