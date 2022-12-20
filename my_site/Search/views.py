from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> This is the Search Engine. </h1>")

def detail(request, location_id):
    return HttpResponse("<h2> You're looking at the Location id :  %s. </h2>" % location_id)
