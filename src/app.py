from flask import Flask
from routes.event_bp import event_bp

app = Flask(__name__)

app.register_blueprint(event_bp, url_prefix='/event')
