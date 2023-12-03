from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Views module is basically the HTTP Request handler.
# It takes a request and gives a response.

def apps_first_resp(request): # By convention it takes request as an argument.
    return HttpResponse("Hello World🌐❣  This is my app's first response.🥇 I believe things are gonna go well.👋")
    # From here we can:
    # Pull data from db
    # Transform data
    # Send email etc.

def templating(request):
    return render(request, 'wsites/form.html')
