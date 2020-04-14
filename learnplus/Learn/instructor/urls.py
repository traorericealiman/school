from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('account_edit', views.account_edit, name='account-edit'),
    path('browse_courses', views.browse_courses, name='browse-courses'),
    path('carts', views.carts, name='cart'),
    path('course_edit', views.course_edit, name='course-edit'),
    path('courses', views.courses, name='courses'),
    path('earnings', views.earnings, name='earnings'),
    path('edit_invoice', views.edit_invoice, name='edit-invoice'),
    path('forum', views.forum, name='forum'),
    path('forum_ask', views.forum_ask, name='forum-ask'),
    path('forum_thread', views.forum_thread, name='forum-thread'),
    path('invoice', views.invoice, name='invoice'),
    path('invoice_settings', views.invoice_settings, name='invoice-settings'),
    path('messages', views.messages, name='messages'),
    path('messages_2', views.messages_2, name='messages-2'),
    path('profile', views.profile, name='profile'),
    path('quiz_edit', views.quiz_edit, name='quiz-edit'),
    path('quiz_results', views.quiz_results, name='quiz-results'),
    path('quizzes', views.quizzes, name='quizzes'),
    path('take_course', views.take_course, name='take-course'),
    path('take_quiz', views.take_quiz, name='take-quiz'),
    path('view_course', views.view_course, name='view-course'),
    
]