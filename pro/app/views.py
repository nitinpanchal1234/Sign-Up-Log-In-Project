from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseBadRequest
# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')
def signup_action(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        bd = request.POST['bd']

        signup_data = User.objects.create(name=name, email=email, password=password, phone=phone, bd=bd)
        
        user_data = User.objects.all()
        dict = {
            'user_data' : user_data
        }
        return render(request, 'signup_show.html', dict)
    
def login(request):
    return render(request, 'login.html')
def login_action(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            login_data = User.objects.get(email=email, password=password)

            user_data_1 = [login_data]
            dict_1 = {
                'user_data_1' : user_data_1
            }
            return render(request, 'login_show.html', dict_1)
        except User.DoesNotExist:
            messages.error('User data  does not found Please sign up or log in again')
            redirect('/login')

        


