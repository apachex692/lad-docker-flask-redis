# Author: Sakthi Santhosh
# Created on: 13/08/2023
from secrets import token_hex

class Config:
    SECRET_KEY = token_hex(16)
