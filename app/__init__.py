from flask import Flask, Request, Response
from flask_admin import  Admin
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate, MigrateCommand







app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
bootstrap = Bootstrap(app)


login_manager.login_view = 'auth.login'
admin = Admin(app, template_mode='bootstrap3')
app.config.from_object('config')




# BluePrints:
from app.auth import auth
app.register_blueprint(auth)

from app.main import main
app.register_blueprint(main)