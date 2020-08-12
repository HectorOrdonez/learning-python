from .models import Package

class PackageRepository():
    def find_all_names():
        return [
            'some-package-1',
            'some-package-2',
            'some-package-3',
            'some-package-4',
            'some-package-5',
        ]

    def find_one():
        package = Package('test1', [
            'some description line 1',
            'some description line 2',
            'some description line 3'
        ], {
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