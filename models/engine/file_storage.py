#!/usr/bin/python3
"""FileStorage class that serializes instances to a JSON file
and deserializes JSON file to instances"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """FileStorage class that serializes instances to a JSON file
       and deserializes JSON file to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """Return all the objects"""
        return (FileStorage.__objects)

    def new(self, obj):
        """Add a new object"""
        if obj is not None:
            FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Save all objects to a json file"""
        ob = {}
        for k in self.__objects:
            ob[k] = self.__objects[k].to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(ob, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                j = json.load(f)
            for key in j:
                self.__objects[key] = classes[j[key]["__class__"]](**j[key])
        except Exception:
            pass
