from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

import os

from .data import db_session
from .data.users import User, Projects

application = Flask(__name__)
application.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')

login_manager = LoginManager()
login_manager.init_app(application)

mail = Mail(application)
CORS(application)

limiter = Limiter(app=application, key_func=get_remote_address)

from .bp_main.main_routs import main_bp
from .bp_create.create_routes import create_bp
from .bp_oauth.oauth_routes import oauth_bp
from .bp_api.api_routs import api_bp
from .bp_errors.errors_routs import errors_bp

application.register_blueprint(errors_bp)
application.register_blueprint(main_bp)
application.register_blueprint(create_bp)
application.register_blueprint(oauth_bp)
application.register_blueprint(api_bp)
