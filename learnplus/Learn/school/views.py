from django.shortcuts import render

# Create your views here.
def login(request):

    datas = {

    }
    return render(request, 'pages/guest-login.html', datas)

def signup(request):

    datas = {

    }
    return render(request, 'pages/guest-signup.html', datas) 

def forgot_password(request):

    datas = {

    }
    return render(request, 'pages/guest-forgot-password.html', datas)