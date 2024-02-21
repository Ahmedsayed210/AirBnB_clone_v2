from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import uuid

Base = declarative_base()

class BaseModel:
    """A base class for all models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    setattr(self, k, v)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Delete the current instance from the storage"""
        from models import storage
        storage.delete(self)



# #!/usr/bin/python3
# """This module defines a base class for all models in our hbnb clone"""
# from sqlalchemy.ext.declarative import declarative_base
# from datetime import datetime
# from typing import Optional
# import sqlalchemy

# Base = declarative_base()
# db = sqlalchemy

# class BaseModel:
#     __tableName__ = ''

#     id = db.Column(db.String(60), primary_key=True)
#     created_at = db.Column(datetime(), default=datetime.utcnow())
#     updated_at = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)


#     @classmethod
#     def new(cls, **kwargs):
#         """Creates a new instance of the class."""
#         instance = cls(**kwargs)
#         cls.save(instance)
#         return instance
    

#     def __init__(self, **kwargs):
#         super().__init__()
#         for attr, value in kwargs.items():
#             setattr(self, attr, value)
#         self.created_at = self.created_at if hasattr(self, 'created_at') else datetime.utcnow()
#         self.updated_at = self.updated_at if hasattr(self, 'updated_at') else datetime.utcnow()

#     def save(self):
#         """Save the instance to the database."""
#         self.updated_at = datetime.utcnow()
#         db.session.add(self)
#         db.session.commit()

#     def to_dict(self):
#         """Represent the instance as a dictionary."""
#         dictionary = {}
#         for col in self.__table__.columns:
#             dictionary[col.name] = getattr(self, col.name)
#         if '_sa_instance_state' in dictionary:
#             del dictionary['_sa_instance_state']
#         return dictionary

#     def delete(self):
#         """Delete the instance from the database."""
#         db.session.delete(self)
#         db.session.commit()
