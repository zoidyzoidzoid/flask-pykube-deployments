from flask import Flask, render_template
from pykube import Deployment, HTTPClient, KubeConfig

api = HTTPClient(KubeConfig.from_file('~/.kube/config'))

app = Flask(__name__)


@app.route('/')
@app.route('/deployments')
def deployments_list():
    deployments = Deployment.objects(api).filter(namespace='default')
    return render_template('deployment_list.html', deployments=deployments)


@app.route('/deployments/<name>')
def deployments_get(name):
    deployment = Deployment.objects(api).get(name=name)
    return render_template('deployment_get.html', deployment=deployment)
