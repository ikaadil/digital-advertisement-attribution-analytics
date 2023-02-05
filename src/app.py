from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_migrate import Migrate

from routes.event_bp import event_bp
from routes.pageview_bp import pageview_bp
from config import db




app = Flask(__name__)
migrate = Migrate(app, db)

app.config.from_object('config')
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


app.register_blueprint(event_bp, url_prefix='/event')
app.register_blueprint(pageview_bp, url_prefix='/pageview')


@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.debug = True
    app.run()
