from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('packages/index.html')

    return HttpResponse(template.render())

def show(request, package_name):
    template = loader.get_template('packages/show.html')

    return HttpResponse(template.render())

