import urllib
import os

class Config(object):
    params = urllib.parse.quote_plus("Driver={SQL Server Native Client 11.0};Server=.;Database=blog;Trusted_Connection=yes;")
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or '$ecretkey'