from django.core import serializers
from django.http import JsonResponse
from .repositories import PackageRepository

def index(request):
    # IOC?
    repository = PackageRepository()

    packages = repository.find_all_names()

    return JsonResponse({'packages': packages})

def show(request, package_name):
    # IOC? 
    repository = PackageRepository()

    # Use serializer?
    package = repository.find_one(package_name)
    data = {
        'name': package.name,
        'description': package.description,
        'dependencies': package.dependencies
    }

    return JsonResponse(data)
