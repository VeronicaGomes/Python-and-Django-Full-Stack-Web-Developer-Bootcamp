from django.shortcuts import render
from appTwo.models import User
from appTwo import forms

# Create your views here.
def index(request):
    return render(request, 'appTwo/index.html', context={})

def sign_up_view(request):
    form = forms.SignUpForm()

    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR: Form is invalid')

    return render(request, 'appTwo/users.html', {'form': form})


# def users(request):
#     users_list = User.objects.order_by('first_name')
#     users_dict = {'users_info': users_list}
#
#     return render(request, 'appTwo/users.html', context=users_dict)
