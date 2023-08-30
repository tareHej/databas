


import psycopg2

from customer import *
from admin import * 


def connectServer():
    connection = psycopg2.connect(
            dbname=""
            username="",
            password="",
            host="pgserver.usab.us",
        )
    return connection