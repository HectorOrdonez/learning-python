import os
from .models import Package
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

class PackageRepository():
    def __init__(self):
        file = open(os.path.join(settings.BASE_DIR, 'packages/storage/status-all-entries'))

        lines = file.readlines()

        self.source = []
        for line in lines:
            raw_data = line.split(': ')
            data = [raw_data[0].strip()]

            if(len(raw_data) > 1):
                data.append(raw_data[1].strip())

            self.source.append(data)

        file.close()

    def find_all_names(self):
        names = []

        for record in self.source:
            if(record[0] == 'Package'):
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
            if(record[0] == 'Package' and record[1] == package_name):
                return True
        return False
                
    # Assumes package exists
    def __get_package_details(self, package_name):
        currentEntry = False
        packageFound = False
        data = {
            'name': package_name,
            'description': [],
            'dependencies': {}
        }

        # First we need to find where the package info starts
        for record in self.source:

            if(record[0] == 'Package'):
                # Package was already found, we are now facing another package
                if (packageFound == True):
                    return data
                
                if (package_name == record[1]): 
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

                if(currentEntry == 'Description'):
                    data['description'].append(currentData)
                elif(currentEntry == 'Depends'):
                    data['dependencies'] = self.__parse_dependencies(currentData)

        print(data)
        return data

    def __parse_dependencies(self, data):
        raw_dependencies = data.split(', ')
        dependencies = []

        for raw_dependency in raw_dependencies:
            data = raw_dependency.split(' ')
            dependency_name = data[0]

            package_exists = self.__package_exists(dependency_name)

            dependencies.append({
                'name': dependency_name,
                'installed': package_exists
            })

        return dependencies
