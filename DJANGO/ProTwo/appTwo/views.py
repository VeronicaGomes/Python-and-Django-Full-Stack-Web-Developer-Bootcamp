from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User

# Create your views here.
def index(request):
    return render(request, 'appTwo/index.html', context={})

def users(request):
    users_list = User.objects.order_by('first_name')
    users_dict = {'users_info': users_list}

    return render(request, 'appTwo/users.html', context=users_dict)
