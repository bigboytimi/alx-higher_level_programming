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

    @staticmethod
    def from_json_string(json_string):
        """return the list of JSON string.

        Args:
            json_string(str): Json string"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantiated from a dictionary of attrributes.

        Args:
            **dictionary (dict): Key/value pairs pf attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of class from Json strings."""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
