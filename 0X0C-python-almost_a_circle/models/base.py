#!/usr/bin/python3
"""Create a class Base."""
import json


class Base:
    """A class called Base."""

    __nb_objects = 0

    def __init__(self, id=None):
        """The definition for class Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json string representation


        Args: 
            list_dictionaries(list): A list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the json representation to file


        Args:
            list_objs(list): A list of inherited Base instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as e:
            if list_objs is None:
                e.write([])
            else:
                list_dicts = [inst.to_dictionary() for inst in list_objs]
                e.write(Base.to_json_string(list_dicts))

