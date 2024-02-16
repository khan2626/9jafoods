#!/usr/bin/python3
"""It defines a class FileStorage"""

import json

class FileStorage:
    """it represents class FileStprage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary __objects"""
        return FileStorage.__objects
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""

        obj_cls_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_cls_name, obj.id)] = obj

    def save(self):
        """serializes __objects to JSON file __file_path"""
        o_dict = FileStorage.__objects
        obj_dict = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes JSON file to __objects""" 
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return


