from django.urls import path
from .views import index
from .views import show

urlpatterns = [
    path('packages', index, name='packages.index'),
    path('packages/<str:package_name>/', show, name='packages.show')
]
