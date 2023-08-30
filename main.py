


import psycopg2

from customer import *
from admin import * 


def connectServer():
    
    try:
        connection = psycopg2.connect(
            user="",
            password="",
            host="pgserver.usab.us",
            database=""
        )
        return connection