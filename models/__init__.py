from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
# models/__init__.py

import os

# Determine the type of storage from environment variable
storage_t = os.getenv('HBNB_TYPE_STORAGE')

# Default to file storage if the environment variable is not set
if storage_t is None:
    storage_t = 'file'
