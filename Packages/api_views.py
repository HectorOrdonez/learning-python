from django.http import JsonResponse

def index(request):
    return JsonResponse({'foo':'bar'})


def show(request, package_name):
    return JsonResponse({'foo':'bar'})
    