from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
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
                return render(request,'pages/instructor-dashboard.html',datas)
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
                return render(request,'pages/instructor-account-edit.html',datas)
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
                return render(request,'pages/instructor-browse-courses.html',datas)
        except:
            print("3")
            return redirect("/admin/")
    

@login_required(login_url = 'login')
def carts(request):
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
                return render(request,'pages/instructor-cart.html',datas)
        except:
            print("3")
            return redirect("/admin/")
   
@login_required(login_url = 'login')
def course_edit(request):
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
                return render(request,'pages/instructor-account-edit.html',datas)
        except:
            print("3")
            return redirect("/admin/")
    datas = {

    }
    return render(request,'pages/instructor-course-edit.html',datas)


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
                return render(request,'pages/instructor-account-edit.html',datas)
        except:
            print("3")
            return redirect("/admin/")
    datas = {

    }
    return render(request,'pages/instructor-courses.html',datas)


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
                return render(request,'pages/instructor-account-edit.html',datas)
        except:
            print("3")
            return redirect("/admin/")
    datas = {

    }
    return render(request,'pages/instructor-earnings.html',datas)

@login_required(login_url = 'login')
def edit_invoice(request):
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
                return render(request,'pages/instructor-edit-invoice.html',datas)
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
                return render(request,'pages/instructor-forum.html',datas)
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
                return render(request,'pages/instructor-forum-ask.html',datas)
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
                return render(request,'pages/instructor-forum-thread.html',datas)
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
                return render(request,'pages/instructor-invoice.html',datas)
        except:
            print("3")
            return redirect("/admin/")
    

@login_required(login_url = 'login')
def invoice_settings(request):
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
                return render(request,'pages/instructor-invoice-settings.html',datas)
        except:
            print("3")
            return redirect("/admin/")
    

@login_required(login_url = 'login')
def lesson_add(request):
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
                return render(request,'pages/instructor-lesson-add.html',datas)
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
                return render(request,'pages/instructor-messages.html',datas)
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
                return render(request,'pages/instructor-messages-2.html',datas)
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
                return render(request,'pages/instructor-my-courses.html',datas)
        except:
            print("3")
  

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
                return render(request,'pages/instructor-profile.html',datas)
        except:
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def quiz_edit(request):
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
                return render(request,'pages/instructor-quiz-edit.html',datas)
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
                return render(request,'pages/instructor-quiz-results.html',datas)
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
                return render(request,'pages/instructor-quizzes.html',datas)
        except:
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def review_quiz(request):
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
                return render(request,'pages/instructor-review-quiz.html',datas)
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
                return render(request,'pages/instructor-take-course.html',datas)
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
                return render(request,'pages/instructor-take-quiz.html',datas)
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
                return render(request,'pages/instructor-view-course.html',datas)
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
                return render(request,'pages/instructor-statement.html',datas)
        except:
            print("3")
            return redirect("/admin/")




