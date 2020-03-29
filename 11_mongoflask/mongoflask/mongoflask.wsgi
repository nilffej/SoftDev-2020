#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/mongoflask/")
sys.path.insert(0,"/var/www/mongoflask/mongoflask/")

import logging
logging.basicConfig(stream=sys.stderr)

from mongoflask import app as application

