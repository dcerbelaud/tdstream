#!/usr/bin/python
# -*-coding:utf-8 -*

import json
from client import Client
from config import *


td_client = Client()

td_client.connect(teleportd_url)

