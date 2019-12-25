
# Python defines two types of packages, regular packages and namespace packages. 
# Regular packages are traditional packages as they existed in Python 3.2 and earlier. 
# A regular package is typically implemented as a directory containing an __init__.py file. 
# When a regular package is imported, this __init__.py file is implicitly executed, 
# and the objects it defines are bound to names in the package’s namespace. 
# The __init__.py file can contain the same Python code that any other module can contain, 
# and Python will add some additional attributes to the module when it is imported.

# https://www.mongard.ir/one_part/23/what-__init__py-file-python/

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from application.config import Config
from application import routes,models , errors
import logging
from logging.handlers import SMTPHandler
from logging.handlers import RotatingFileHandler
import os


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)




if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Rick Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
        
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/Rick.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Rick startup')