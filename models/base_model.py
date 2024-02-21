#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import column
from datetime import datetime
from typing import Optional

Base = declarative_base()
db = declarative_base()

class BaseModel:
    __tableName__ = ''
    id = db.Column(db.String(60), primary_key=True)
