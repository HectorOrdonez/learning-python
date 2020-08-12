from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .repositories import PackageRepository

def index(request):
    # IOC?
    repository = PackageRepository()

    packages = repository.find_all_names()

    return render(request, 'packages/index.html', {'packages': packages})

def show(request, package_name):
    # IOC? 
    repository = PackageRepository()
    package = repository.find_one(package_name)

    return render(request, 'packages/show.html', {'package': package})
