from django.http import HttpResponse


def error_404(request):
    return HttpResponse("<h1>Not Found </h1>")
