from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<em>My Second Project</em>");

def help(request):
    dictionary = {'insert' : 'HELP PAGE'}
    return render(request, 'appTwo/help.html', context=dictionary)
