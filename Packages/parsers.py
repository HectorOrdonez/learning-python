class PackageParser():

    def parse(self, source, package_name):
        currentEntry = False
        packageFound = False
        data = {
            'name': package_name,
            'description': [],
            'dependencies': {}
        }

        # First we need to find where the package info starts
        for record in source:

            if record[0] == 'Package':
                # Package was already found, we are now facing another package
                if packageFound == True:
                    return data
                
                if package_name == record[1]: 
                    # This is the package we are looking for!
                    packageFound = True;
                    continue

            if packageFound == True:
                # adding data
                if len(record) > 1:
                    currentEntry = record[0]
                    currentData = record[1]
                else:
                    currentData = record[0]

                if currentEntry == 'Description':
                    data['description'].append(currentData)
                elif(currentEntry == 'Depends'):
                    data['dependencies'] = self.__parse_dependencies(currentData)


    def __parse_dependencies(self, data):
        raw_dependencies = data.split(', ')
        dependencies = []

        for raw_dependency in raw_dependencies:
            data = raw_dependency.split(' ')
            dependency_name = data[0]

            dependencies.append({
                'name': dependency_name
            })

        return dependencies
