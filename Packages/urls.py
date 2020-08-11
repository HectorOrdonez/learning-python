from django.urls import path
from .web_views import index as web_index
from .web_views import show as web_show
from .api_views import index as api_index
from .api_views import show as api_show

urlpatterns = [
    # Web routes
    path('packages', web_index, name='packages.index'),
    path('packages/<str:package_name>/', api_show, name='packages.show'),

    # Api routes
    path('api/v1/packages', api_index, name='api.v1.packages.index'),
    path('api/v1/packages/<str:package_name>/', api_show, name='api.v1.packages.show')

]
