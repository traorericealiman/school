from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'login')
def index(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-dashboard.html',datas)
        except:
            print("3")
            return redirect("/admin/")


@login_required(login_url = 'login')
def payment(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-account-billing-payment-information.html',datas)
        except:
            print("3")
            return redirect("/admin/")
   
@login_required(login_url = 'login')
def subscription(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-account-billing-subscription.html',datas)
        except:
            print("3")
            return redirect("/admin/")
    
@login_required(login_url = 'login')
def upgrade(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-account-billing-upgrade.html',datas)
        except:
            print("3")
            return redirect("/admin/")
    

@login_required(login_url = 'login')
def edit(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-account-edit.html',datas)
        except:
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def edit_basic(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-account-edit-basic.html',datas)
        except:
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def edit_profile(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-account-edit-profile.html',datas)
        except:
            print("3")
            return redirect("/admin/")


@login_required(login_url = 'login')
def billing(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-billing.html',datas)
        except:
            print("3")
            return redirect("/admin/")
    
@login_required(login_url = 'login')
def browse_courses(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-browse-courses.html',datas)
        except:
            print("3")
            return redirect("/admin/")
   

@login_required(login_url = 'login')
def cart(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-cart.html',datas)
        except:
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def courses(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-courses.html',datas)
        except:
            print("3")
            return redirect("/admin/")
    
@login_required(login_url = 'login')
def dashboard(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-dashboard.html',datas)
        except:
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def earnings(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-earnings.html',datas)
        except:
            print("3")
            return redirect("/admin/")


@login_required(login_url = 'login')
def forum(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-forum.html',datas)
        except:
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def forum_ask(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-forum-ask.html',datas)
        except:
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def forum_thread(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-forum-thread.html',datas)
        except:
            print("3")
            return redirect("/admin/")
    

@login_required(login_url = 'login')
def help_center(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-help-center.html',datas)
        except:
            print("3")
            return redirect("/admin/")
    

@login_required(login_url = 'login')
def invoice(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-invoice.html',datas)
        except:
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def messages(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-messages.html',datas)
        except:
            print("3")
            return redirect("/admin/")
    
@login_required(login_url = 'login')
def messages_2(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-messages-2.html',datas)
        except:
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def my_courses(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-my-courses.html',datas)
        except:
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def pay(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-pay.html',datas)
        except:
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def profile(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-profile.html',datas)
        except:
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def profile_posts(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-profile-posts.html',datas)
        except:
            print("3")
            return redirect("/admin/")
    

@login_required(login_url = 'login')
def quiz_results(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-quiz-results.html',datas)
        except:
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def quizzes(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-quizzes.html',datas)
        except:
            print("3")
            return redirect("/admin/")
    

@login_required(login_url = 'login')
def statement(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-statement.html',datas)
        except:
            print("3")
            return redirect("/admin/")
    

@login_required(login_url = 'login')
def student_take_course(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-student-take-course.html',datas)
        except:
            print("3")
            return redirect("/admin/")
   
@login_required(login_url = 'login')
def take_course(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-take-course.html',datas)
        except:
            print("3")
            return redirect("/admin/")
   

@login_required(login_url = 'login')
def take_quiz(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-take-quiz.html',datas)
        except:
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def view_course(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-view-course.html',datas)
        except:
            print("3")
            return redirect("/admin/")
    
@login_required(login_url = 'login')
def account_edit(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/fixed-student-account-edit.html',datas)
        except:
            print("3")
            return redirect("/admin/")
    