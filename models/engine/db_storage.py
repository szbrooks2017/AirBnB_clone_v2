import sys
from sqlalchemy import (create_engine)

class DBStorage:
    """DBStorage creates the engine connected to hbnb_dev_db"""
    __engine=None
    __session=None
    
    def __init__(self):
        self.__engine = create_engine(('mysql+mysqldb://{}:{}@{}/{}'
                           .format(HBNB_MYSQL_USER,
                                   HBNB_MYSQL_PWD,
                                   HBNB_mYSQL_HOST,
                                   HBNB_MYSQL_DB
                                   pool_pre_ping=True))
        if HBNB_ENV is test:
            DROP ALL TABLES:

#cascade() / delete_orphan()
