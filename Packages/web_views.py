from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

def index(request):
    packages = [
        'some',
        'names',
        'here'
    ]

    return render(request, 'packages/index.html', {'packages': packages})

def show(request, package_name):
    package = {
        'name': package_name,
        'description': [
        'some description line 1',
        'some description line 2',
        'some description line 3'
        ],
        'dependencies': {
            'dependency1': {
                'name': 'dependency-1',
                'reference': 'some-reference',
            },
            'dependency2': {
                'name': 'dependency-2',
                'reference': 'some-reference-2',
            }
        }
    }

    return render(request, 'packages/show.html', {'package': package})

