#!/usr/bin/python3
"""define class"""
import os
import sys
from sqlalchemy import MetaData, create_engine

class DBStorage:
    """DBStorage creates the engine connected to hbnb_dev_db"""
    __engine=None
    __session=None
    
    def __init__(self):

        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(('mysql+mysqldb://{}:{}@{}/{}'
                           .format(user,
                                   password,
                                   host,
                                   database),
                                   pool_pre_ping=True))
        if os.getenv('HBNB_ENV') is test:
            Base.metadata.drop_all(bind=self.__engine)

#cascade() / delete_orphan()
