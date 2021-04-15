import os
import configparser

class Config(object):
	config = configparser.ConfigParser()
	config.read_file(open('app.cfg'))
	SECRET_KEY = config['FLASK']['SECRET_KEY']