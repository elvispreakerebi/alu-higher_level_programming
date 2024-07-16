#!/usr/bin/python3
""" This is the script """


class Student:
    """
    A class that defines a student with attributes: first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list of str or None): If a list of strings, retrieve only the attributes
                listed in attrs. If None, retrieve all attributes.

        Returns:
            dict: A dictionary containing the selected attributes of the Student instance.
        """
        if attrs is None:
            # If attrs is None, retrieve all attributes
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            # Filter and retrieve only the attributes listed in attrs
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on a dictionary.

        Args:
            json (dict): A dictionary where keys are attribute names and values are attribute values.

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
