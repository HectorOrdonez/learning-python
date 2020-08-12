from django.db import models

class Package():
    def __init__(self, name, description, dependencies):
        self.name = name
        self.description = description
        self.dependencies = dependencies
