import os
import configparser
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
	config = configparser.ConfigParser()
	config.read_file(open('app.cfg'))
	SECRET_KEY = os.environ.get('SECRET_KEY') or config['FLASK']['SECRET_KEY']
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False