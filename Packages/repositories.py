import os
from .models import Package
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

class PackageRepository():
    def __init__(self):
        file = open(os.path.join(settings.BASE_DIR, 'packages/storage/status-1-entry'))

        data = file.readlines()

        self.source = []
        for record in data:
            self.source.append(record.split(': '))

        file.close()

    def find_all_names(self):
        names = []

        for record in self.source:
            if(record[0] == 'Package'):
                names.append(record[1])

        return names

    def find_one(self, package_name):
        if not self.__package_exists:
            raise ObjectDoesNotExist('package does not exist')

        details = self.__get_package_details(package_name)

        package = Package(details['name'], details['description'], {
            'dependency-1': {
                'name': 'name1',
                'reference': 'some-ref'
            },
            'dependency-2': {
                'name': 'name2',
                'reference': 'some-ref'
            }
        })

        return package

    def __package_exists(package_name):        
        for record in self.source:
            if(record[0] == 'Package' and record[1] == package_name):
                return True
        return False
                
    # Assumes package exists
    def __get_package_details(self, package_name):
        currentEntry = 'none'
        packageFound = False;
        data = {
            'name': package_name,
            'description': [],
            'dependencies': {}
        }

        # First we need to find where the package info starts
        for record in self.source:

            if(record[0].strip() == 'Package'):
                # Package was already found, we are now facing another package
                if (packageFound == True):
                    return data
                
                if (package_name == record[1].strip()): 
                    # This is the package we are looking for!
                    packageFound = True;
                    continue

            if (packageFound == True):
                # adding data
                if len(record) > 1:
                    currentEntry = record[0]
                    currentData = record[1]
                else:
                    currentData = record[0]

                if(currentEntry.strip() == 'Description'):
                    data['description'].append(currentData);

        return data
