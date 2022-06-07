from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_migrate import Migrate
import os 

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

db = SQLAlchemy()
jwt = JWTManager()
mail = Mail()
migrate = Migrate()

def create_app():
  app = Flask(__name__)

  app.config['SECRET_KEY'] = 'etdlearning'
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql12436516:8bkZZJxYGS@sql12.freemysqlhosting.net/sql12436516'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
  app.config['MAIL_PORT'] = 587
  app.config['MAIL_USE_TLS'] = True
  app.config['MAIL_USERNAME'] = 'portalpps.etdhtaa@gmail.com'
  app.config['MAIL_PASSWORD'] = "PPSetdht@@"

  db.init_app(app)

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)
  

  jwt.init_app(app)
  mail.init_app(app)
  migrate.init_app(app,db)

  from .models import User, OAuth

  @login_manager.user_loader
  def load_user(user_id):
    return User.query.get(int(user_id))

  #blueprints auth routes
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint.auth)

  #non-auth parts
  from .mainframe import mainframe as mainframe_blueprint
  app.register_blueprint(mainframe_blueprint.mainframe)

  return app