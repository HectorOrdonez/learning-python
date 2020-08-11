# pages/views.py
from django.http import HttpResponse

def homePackageView(request):
    return HttpResponse('Hello, packages!')
