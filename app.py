from flask import Flask,render_template
from flask_migrate import Migrate
from blueprints.register import bp as user_bp
import config
from model import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

migrate = Migrate(app,db)
app.register_blueprint(user_bp)

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
