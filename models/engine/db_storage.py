from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State

class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = []
            for cls in [State, City]:
                objs += self.__session.query(cls).all()
        return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in objs}

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                      expire_on_commit=False))

    def close(self):
        """Close the current session"""
        self.__session.close()


# #!/usr/bin/python3
# """ DBStorage: class from db storage """
# import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, scoped_session


# class DBStorage:
#     """ DBStorage: class from db storage """
#     __engine = None
#     __session = None

#     def __init__(self):
#         """ initialize instance """
#         usr = os.environ.get('HBNB_MYSQL_USER')
#         ps = os.environ.get('HBNB_MYSQL_PWD')
#         host = os.environ.get('HBNB_MYSQL_HOST')
#         db = os.environ.get('HBNB_MYSQL_DB')
#         statement = f"mysql+mysqldb://{usr}:{ps}@{host}/{db}"
#         self.__engine = create_engine(f"{statement}",
#                                       pool_pre_ping=True)
#         if os.environ.get('HBNB_ENV') == 'test':
#             from models.base_model import Base
#             Base.metadata.drop_all(self.__engine)

#     def all(self, cls=None):
#         """ all """
#         from models.user import User
#         from models.place import Place
#         from models.state import State
#         from models.city import City
#         from models.amenity import Amenity
#         from models.review import Review
#         my_dict = {}
#         if cls is None:
#             all_objs = self.__session.query(User, State, City,
#                                             Amenity, Place, Review)\
#                                      .all()
#         else:
#             all_objs = self.__session.query(cls).all()

#         for obj in all_objs:
#             my_dict[(str(type(obj)).split('.')[-1])
#                     .split('\'')[0] + '.' + obj.id] = obj
#         return my_dict

#     def new(self, obj):
#         """ add new object """
#         self.__session.add(obj)

#     def save(self):
#         """ save commits """
#         self.__session.commit()

#     def delete(self, obj=None):
#         """ delete obj using the session """
#         if obj is not None:
#             self.__session.delete(obj)

#     def reload(self):
#         """ reload db """
#         from models.base_model import Base
#         Base.metadata.create_all(self.__engine)
#         session_factory = sessionmaker(bind=self.__engine,
#                                        expire_on_commit=False)
#         Session = scoped_session(session_factory)
#         self.__session = Session()

#     def close(self):
#         """ call remove method on a private session """
#         if self.__session:
#             self.__session.close()
