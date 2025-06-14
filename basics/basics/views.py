from django.http import HttpResponse 

def hello_msg(request):
    return HttpResponse("This is the basic project")

