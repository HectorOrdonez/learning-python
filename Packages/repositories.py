import os
from .models import Package
from django.conf import settings
from .parsers import PackageParser
from django.core.exceptions import ObjectDoesNotExist

class PackageRepository():
    def __init__(self):
        self.parser = PackageParser()

        file = open(os.path.join(settings.BASE_DIR, 'packages/storage/status-all-entries'))
        lines = file.readlines()
        file.close()

        self.source = []
        for line in lines:
            raw_data = line.split(': ')
            data = [raw_data[0].strip()]

            if len(raw_data) > 1:
                data.append(raw_data[1].strip())

            self.source.append(data)


    def find_all_names(self):
        names = []

        for record in self.source:
            if record[0] == 'Package':
                names.append(record[1])

        return names

    def find_one(self, package_name):
        if not self.__package_exists(package_name):
            raise ObjectDoesNotExist('package ' + package_name +' does not exist')

        details = self.__get_package_details(package_name)

        package = Package(details['name'], details['description'], details['dependencies'])

        return package

    def __package_exists(self, package_name):        
        for record in self.source:
            if record[0] == 'Package' and record[1] == package_name:
                return True
        return False
                
    # Assumes package exists
    def __get_package_details(self, package_name):
        details = self.parser.parse(self.source, package_name)

        for dependency in details['dependencies']:
            package_exists = self.__package_exists(dependency['name'])
            dependency['installed'] = package_exists

        return details