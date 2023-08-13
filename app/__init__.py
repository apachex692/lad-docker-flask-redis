# Author: Sakthi Santhosh
# Created on: 13/08/2023
from flask import Flask
from redis import Redis

from app.config import Config

app_handle = Flask(__name__)
app_handle.config.from_object(Config)

redis_handle = Redis(host="redis", port=6379, decode_responses=True)

import app.routes
