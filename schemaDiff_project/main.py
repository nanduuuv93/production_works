import os
import pathlib
import pandas
import mysql.connector as mysql
import json
from json import JSONDecodeError
from datetime import datetime
import logging
import shutil
import pathlib as pl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from schemaDiff_project.log_module import *

logger_c = logging.getLogger('schemaDiff')
logger_c.setLevel(logging.DEBUG)
log_format = logging.Formatter(f'%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
consoleHandler.setFormatter(log_format)
logger_c.addHandler(consoleHandler)

schema_config = {'host': 'localhost',
                 'port': '3306',
                 'user': 'schemaUser',
                 'password': 'schemaUser@@1',
                 'database': 'write_bucket'}

# Directory Paths

reports_path = pl.Path('/home/nandagopal/reports/')
cur_schema_dir = pl.Path.joinpath(reports_path, 'cur_schema_dir')
new_schema_dir = pl.Path.joinpath(reports_path, 'new_schema_dir')
bkp_schema_dir = pl.Path.joinpath(reports_path, 'bkp_schema_dir')