from django.shortcuts import render

# Create your views here.
def guest_login(request):

    datas = {

    }
    return render(request, 'pages/guest-login.html', datas)

def guest_signup(request):

    datas = {

    }
    return render(request, 'pages/guest-signup.html', datas) 

def guest_forgot_password(request):

    datas = {

    }
    return render(request, 'pages/guest-forgot-password.html', datas)