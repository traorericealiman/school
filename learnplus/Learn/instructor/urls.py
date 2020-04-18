from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('account_edit', views.account_edit, name='instructor-account-edit'),
    path('browse_courses', views.browse_courses, name='instructor-browse-courses'),
    path('carts', views.carts, name='cart'),
    path('course_edit', views.course_edit, name='course-edit'),
    path('courses', views.courses, name='instructor-courses'), 
    path('earnings', views.earnings, name='earning'),
    path('edit_invoice', views.edit_invoice, name='instructor-edit-invoice'),
    path('forum', views.forum, name='instructor-forum'),
    path('forum_ask', views.forum_ask, name='instructor-forum-ask'),
    path('forum_thread', views.forum_thread, name='instructor-forum-thread'),
    path('invoice', views.invoice, name='instructor-invoice'),
    path('invoice_settings', views.invoice_settings, name='instructor-invoice-settings'),
    path('messages', views.messages, name='instructor-messages'),
    path('messages_2', views.messages_2, name='instructor-messages-2'),
    path('profile', views.profile, name='instructor-profile'),
    path('quiz_edit', views.quiz_edit, name='instructor-quiz-edit'),
    path('quiz_results', views.quiz_results, name='instructor-quiz-results'),
    path('quizzes', views.quizzes, name='instructor-quizzes'),
    path('take_course', views.take_course, name='instructor-take-course'),
    path('take_quiz', views.take_quiz, name='instructor-take-quiz'),
    path('view_course', views.view_course, name='instructor-view-course'),
    path('statement', views.statement, name='instructor-statement'),
    
]