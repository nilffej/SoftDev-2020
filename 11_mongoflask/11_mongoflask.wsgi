#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/11_mongoflask/")
sys.path.insert(0,"/var/www/11_mongoflask/11_mongoflask/")

import logging
logging.basicConfig(stream=sys.stderr)

from 11_mongoflask import app as application
