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

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from application import routes,models


