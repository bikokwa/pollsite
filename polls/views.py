from django.http import HttpResponse

#display a message to the world
def index(request):
    return HttpResponse("Hello world. This is a polls site.")
