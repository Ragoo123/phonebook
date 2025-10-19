from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf import CSRFProtect
from flask_htmx import HTMX
from flask_bootstrap import Bootstrap5

# Initialize extensions (no app yet)
db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
csrf = CSRFProtect()
htmx = HTMX()
bootstrap = Bootstrap5()
