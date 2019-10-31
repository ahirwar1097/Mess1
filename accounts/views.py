from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
#from .models import Student, FeeDetails, Mess, MessAllot
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
           # messages.info(request, 'logged in')
        else:
            messages.info(request, 'bad credentials')
    else:
        return render(request, 'login.html')


# def register(request):
#     if request.method == 'POST':
#         f_name = request.POST['f_name']
#         l_name = request.POST['l_name']
#         username = request.POST['username']
#         password = request.POST['password']
#         password1 = request.POST['password1']
#
#         if password == password1:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, 'User already exist')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=username, password=password, first_name=f_name, last_name=l_name)
#                 user.save();
#                 messages.info(request, 'User created')
#         else:
#             messages.info(request, 'Password not matching')
#             return redirect('register')
#         return redirect('/')
#     else:
#         return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')



