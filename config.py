import os


class Config(object):
    SECRET_KEY = ' kfjanfjkanfanfjknaf'

    # Database Configuration
    SQLALCHEMY_TRACK_MODIFICATIONS = False    

    # Mail Configuration
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.getenv('EMAIL_USER')
    MAIL_PASSWORD = os.getenv('EMAIL_PASS')
    MAIL_DEFAULT_SENDER = 'OurTeez<{}>'.format(os.getenv('EMAIL_USER'))


class Debug(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    DEBUG = True


class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:password@localhost/database'
    DEBUG = False


config_dict = {'Debug': Debug, 'Production': Production}