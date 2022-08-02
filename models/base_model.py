#!/usr/bin/python3

"""docstrings for base_model"""

import uuid
from datetime import datetime, date


class BaseModel(object):
    """BaseModel class defines all common
    attributes/methods for other classes"""
    def __init__(self):
        """initialization function"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """specially formatted string represntation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the 'updated_at' attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """dictionary representation of object"""
        return_value = {}
        r = return_value    # Aliasing 'return_value'
        for k, v in self.__dict__.items():
            return_value[k] = v
        return_value['__class__'] = self.__class__.__name__
        r['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        r['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return return_value
