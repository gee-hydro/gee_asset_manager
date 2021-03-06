# -*- coding: utf-8 -*-

__author__ = 'Lukasz Tracewski'
__email__ = 'lukasz.tracewski@outlook.com'
VERSION = (0, 1, 6)
__version__ = ".".join([str(x) for x in VERSION])

from gee_asset_manager.batch_remover import delete
from gee_asset_manager.batch_uploader import *  # upload
from gee_asset_manager.config import setup_logging
