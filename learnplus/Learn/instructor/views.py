from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'login')
def dashboard(request):
    datas = {

    }
    return render(request,'pages/instructor-dashboard.html',datas)

@login_required(login_url = 'login')
def account_edit(request):
    datas = {

    }
    return render(request,'pages/instructor-account-edit.html',datas)

@login_required(login_url = 'login')
def browse_courses(request):
    datas = {

    }
    return render(request,'pages/instructor-browse-courses.html',datas)

@login_required(login_url = 'login')
def carts(request):
    datas = {

    }
    return render(request,'pages/instructor-cart.html',datas)

@login_required(login_url = 'login')
def course_edit(request):
    datas = {

    }
    return render(request,'pages/instructor-course-edit.html',datas)


@login_required(login_url = 'login')
def courses(request):
    datas = {

    }
    return render(request,'pages/instructor-courses.html',datas)

    datas = {

    }
    return render(request,'pages/instructor-dashboardx.html',datas)

@login_required(login_url = 'login')
def earnings(request):
    datas = {

    }
    return render(request,'pages/instructor-earnings.html',datas)

@login_required(login_url = 'login')
def edit_invoice(request):
    datas = {

    }
    return render(request,'pages/instructor-edit-invoice',datas)

@login_required(login_url = 'login')
def forum(request):
    datas = {

    }
    return render(request,'pages/instructor-forum.html',datas)

@login_required(login_url = 'login')
def forum_ask(request):
    datas = {

    }
    return render(request,'pages/instructor-forum-ask.html',datas)

@login_required(login_url = 'login')
def forum_thread(request):
    datas = {

    }
    return render(request,'pages/instructor-forum-thread.html',datas)

@login_required(login_url = 'login')
def invoice(request):
    datas = {

    }
    return render(request,'pages/instructor-invoice.html',datas)

@login_required(login_url = 'login')
def invoice_settings(request):
    datas = {

    }
    return render(request,'pages/instructor-invoice-settings.html',datas)

@login_required(login_url = 'login')
def lesson_add(request):
    datas = {

    }
    return render(request,'pages/instructor-lesson-add.html',datas)

@login_required(login_url = 'login')
def messages(request):
    datas = {

    }
    return render(request,'pages/instructor-messages.html',datas)

@login_required(login_url = 'login')
def messages_2(request):
    datas = {

    }
    return render(request,'pages/instructor-messages-2.html',datas)

@login_required(login_url = 'login')
def my_courses(request):
    datas = {

    }
    return render(request,'pages/instructor-my-courses.html',datas)

@login_required(login_url = 'login')
def profile(request):
    datas = {

    }
    return render(request,'pages/instructor-profile.html',datas)

@login_required(login_url = 'login')
def quiz_edit(request):
    datas = {

    }
    return render(request,'pages/instructor-quiz-edit.html',datas)

@login_required(login_url = 'login')
def quiz_results(request):
    datas = {

    }
    return render(request,'pages/instructor-quiz-results.html',datas)

@login_required(login_url = 'login')
def quizzes(request):
    datas = {

    }
    return render(request,'pages/instructor-quizzes.html',datas)

@login_required(login_url = 'login')
def review_quiz(request):
    datas = {

    }
    return render(request,'pages/instructor-review-quiz.html',datas)

@login_required(login_url = 'login')
def statement(request):
    datas = {

    }
    return render(request,'pages/instructor-statementr.html',datas)

@login_required(login_url = 'login')
def take_course(request):
    datas = {

    }
    return render(request,'pages/instructor-take-course.html',datas)

@login_required(login_url = 'login')
def take_quiz(request):
    datas = {

    }
    return render(request,'pages/instructor-take-quiz.html',datas)

@login_required(login_url = 'login')
def view_course(request):
    datas = {

    }
    return render(request,'pages/instructor-view-course.html',datas)




