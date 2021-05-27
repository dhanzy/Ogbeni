from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_admin import Admin, AdminIndexView
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from sqlalchemy import MetaData

## Database ##
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


# db = SQLAlchemy(metadata=MetaData(naming_convention=convention))
db = SQLAlchemy()

## Mail ##
mail = Mail()

## Admin ##
admin = Admin(base_template='site-templates/admin_layout.html')

## Login and security ##
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'

bcrypt = Bcrypt()

def register_extension(app):
    db.init_app(app)
    mail.init_app(app)
    admin.init_app(app, index_view=AdminIndexView(menu_icon_type='fa', menu_icon_value='tv',  name='Dashboard'))
    login_manager.init_app(app) 
    bcrypt.init_app(app)



def register_blueprint(app):
    from Obeni.main.routes import main
    from Obeni.admins.routes import admins

    app.register_blueprint(main)
    app.register_blueprint(admins)

    

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extension(app)
    register_blueprint(app)
    return app