from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'login')
def index(request):

    datas = {

    }
    return render(request, 'pages/fixed-student-dashboard.html', datas)

@login_required(login_url = 'login')
def payment(request):
    datas = {

    }
    return render(request,'pages/fixed-student-account-billing-payment-information.html',datas)

@login_required(login_url = 'login')
def subscription(request):
    datas = {

    }
    return render(request,'pages/fixed-student-account-billing-subscription.html',datas)

@login_required(login_url = 'login')
def upgrade(request):
    datas = {

    }
    return render(request,'pages/fixed-student-account-billing-upgrade.html',datas)

@login_required(login_url = 'login')
def edit(request):
    datas = {

    }
    return render(request,'pages/fixed-student-account-edit.html',datas)

@login_required(login_url = 'login')
def edit_basic(request):
    datas = {

    }
    return render(request,'pages/fixed-student-account-edit-basic.html',datas)

@login_required(login_url = 'login')
def edit_profile(request):
    datas = {

    }
    return render(request,'pages/fixed-student-account-edit-profile.html',datas)

@login_required(login_url = 'login')
def billing(request):
    datas = {

    }
    return render(request,'pages/fixed-student-billing.html',datas)

@login_required(login_url = 'login')
def browse_courses(request):
    datas = {

    }
    return render(request,'pages/fixed-student-browse-courses.html',datas)

@login_required(login_url = 'login')
def cart(request):
    datas = {

    }
    return render(request,'pages/fixed-student-cart.html',datas)

@login_required(login_url = 'login')
def courses(request):
    datas = {

    }
    return render(request,'pages/fixed-student-courses.html',datas)

@login_required(login_url = 'login')
def dashboard(request):
    datas = {

    }
    return render(request,'pages/fixed-student-dashboard.html',datas)

@login_required(login_url = 'login')
def earnings(request):
    datas = {

    }
    return render(request,'pages/fixed-student-earnings.html',datas)


@login_required(login_url = 'login')
def forum(request):
    datas = {

    }
    return render(request,'pages/fixed-student-forum.html',datas)

@login_required(login_url = 'login')
def forum_ask(request):
    datas = {

    }
    return render(request,'pages/fixed-student-forum-ask.html',datas)

@login_required(login_url = 'login')
def forum_thread(request):
    datas = {

    }
    return render(request,'pages/fixed-student-forum-thread.html',datas)

@login_required(login_url = 'login')
def help_center(request):
    datas = {

    }
    return render(request,'pages/fixed-student-help-center.html',datas)

@login_required(login_url = 'login')
def invoice(request):
    datas = {

    }
    return render(request,'pages/fixed-student-invoice.html',datas)

@login_required(login_url = 'login')
def messages(request):
    datas = {

    }
    return render(request,'pages/fixed-student-messages.html',datas)

@login_required(login_url = 'login')
def messages_2(request):
    datas = {

    }
    return render(request,'pages/fixed-student-messages-2.html',datas)

@login_required(login_url = 'login')
def my_courses(request):
    datas = {

    }
    return render(request,'pages/fixed-student-my-courses.html',datas)

@login_required(login_url = 'login')
def pay(request):
    datas = {

    }
    return render(request,'pages/fixed-student-pay.html',datas)

@login_required(login_url = 'login')
def profile(request):
    datas = {

    }
    return render(request,'pages/fixed-student-profile.html',datas)

@login_required(login_url = 'login')
def profile_posts(request):
    datas = {

    }
    return render(request,'pages/fixed-student-profile-posts.html',datas)

@login_required(login_url = 'login')
def quiz_results(request):
    datas = {

    }
    return render(request,'pages/fixed-student-quiz-results.html',datas)

@login_required(login_url = 'login')
def quizzes(request):
    datas = {

    }
    return render(request,'pages/fixed-student-quizzes.html',datas)
    

@login_required(login_url = 'login')
def statement(request):
    datas = {

    }
    return render(request,'pages/fixed-student-statement.html',datas)

@login_required(login_url = 'login')
def student_take_course(request):
    datas = {

    }
    return render(request,'pages/fixed-student-student-take-course.html',datas)

@login_required(login_url = 'login')
def take_course(request):
    datas = {

    }
    return render(request,'pages/fixed-student-take-course.html',datas)

@login_required(login_url = 'login')
def take_quiz(request):
    datas = {

    }
    return render(request,'pages/fixed-student-take-quiz.html',datas)

@login_required(login_url = 'login')
def view_course(request):
    datas = {

    }
    return render(request,'pages/fixed-student-view-course.html',datas)

@login_required(login_url = 'login')
def account_edit(request):
    datas = {

    }
    return render(request,'pages/fixed-student-account-edit.html',datas)
