#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from typing import Optional
import sqlalchemy

Base = declarative_base()
db = sqlalchemy

class BaseModel:
    __tableName__ = ''

    id = db.Column(db.String(60), primary_key=True)
    created_at = db.Column(datetime(), default=datetime.utcnow())
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)


    @classmethod
    def new(cls, **kwargs):
        """Creates a new instance of the class."""
        instance = cls(**kwargs)
        cls.save(instance)
        return instance
    

    def __init__(self, **kwargs):
        super().__init__()
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        self.created_at = self.created_at if hasattr(self, 'created_at') else datetime.utcnow()
        self.updated_at = self.updated_at if hasattr(self, 'updated_at') else datetime.utcnow()

    def save(self):
        """Save the instance to the database."""
        self.updated_at = datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        """Represent the instance as a dictionary."""
        dictionary = {}
        for col in self.__table__.columns:
            dictionary[col.name] = getattr(self, col.name)
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Delete the instance from the database."""
        db.session.delete(self)
        db.session.commit()




# !/usr/bin/python3
# """This module defines a base class for all models in our hbnb clone"""
# import uuid
# from datetime import datetime


# class BaseModel:
#     """A base class for all hbnb models"""
#     def __init__(self, *args, **kwargs):
#         """Instatntiates a new model"""
#         if not kwargs:
#             from models import storage
#             self.id = str(uuid.uuid4())
#             self.created_at = datetime.now()
#             self.updated_at = datetime.now()
#             storage.new(self)
#         else:
#             kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
#                                                      '%Y-%m-%dT%H:%M:%S.%f')
#             kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
#                                                      '%Y-%m-%dT%H:%M:%S.%f')
#             del kwargs['__class__']
#             self.__dict__.update(kwargs)

#     def __str__(self):
#         """Returns a string representation of the instance"""
#         cls = (str(type(self)).split('.')[-1]).split('\'')[0]
#         return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

#     def save(self):
#         """Updates updated_at with current time when instance is changed"""
#         from models import storage
#         self.updated_at = datetime.now()
#         storage.save()

#     def to_dict(se"""This module defines a base class for all models in our hbnb clone"""
# import uuid
# from datetime import datetime


# class BaseModel:
#     """A base class for all hbnb models"""
#     def __init__(self, *args, **kwargs):
#         """Instatntiates a new model"""
#         if not kwargs:
#             from models import storage
#             self.id = str(uuid.uuid4())
#             self.created_at = datetime.now()
#             self.updated_at = datetime.now()
#             storage.new(self)
#         else:
#             kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
#                                                      '%Y-%m-%dT%H:%M:%S.%f')
#             kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
#                                                      '%Y-%m-%dT%H:%M:%S.%f')
#             del kwargs['__class__']
#             self.__dict__.update(kwargs)

#     def __str__(self):
#         """Returns a string representation of the instance"""
#         cls = (str(type(self)).split('.')[-1]).split('\'')[0]
#         return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

#     def save(self):
#         """Updates updated_at with current time when instance is changed"""
#         from models import storage
#         self.updated_at = datetime.now()
#         storage.save()

#     def to_dict(self):
#         """Convert instance into dict format"""
#         dictionary = {}
#         dictionary.update(self.__dict__)
#         dictionary.update({'__class__':
#                           (str(type(self)).split('.')[-1]).split('\'')[0]})
#         dictionary['created_at'] = self.created_at.isoformat()
#         dictionary['updated_at'] = self.updated_at.isoformat()
#         return dictionarylf):
#         """Convert instance into dict format"""
#         dictionary = {}
#         dictionary.update(self.__dict__)
#         dictionary.update({'__class__':
#                           (str(type(self)).split('.')[-1]).split('\'')[0]})
#         dictionary['created_at'] = self.created_at.isoformat()
#         dictionary['updated_at'] = self.updated_at.isoformat()
#         return dictionary