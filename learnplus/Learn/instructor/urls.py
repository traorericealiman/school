from django.urls import path
from . import views

urlpatterns = [
    path('', views.instructor_dashboard, name='instructor-dashboard'),
    path('instructor_account_edit', views.instructor_account_edit, name='instructor-account-edit'),
    path('instructor_browse_courses', views.instructor_browse_courses, name='instructor-browse-courses'),
    path('instructor_carts', views.instructor_carts, name='instructor-cart'),
    path('instructor_course_edit', views.instructor_course_edit, name='instructor-course-edit'),
    path('instructor_courses', views.instructor_courses, name='instructor-courses'),
    path('instructor_earnings', views.instructor_earnings, name='instructor-earnings'),
    path('instructor_edit_invoice', views.instructor_edit_invoice, name='instructor-edit-invoice'),
    path('instructor_forum', views.instructor_forum, name='instructor-forum'),
    path('instructor_forum_ask', views.instructor_forum_ask, name='instructor-forum-ask'),
    path('instructor_forum_thread', views.instructor_forum_thread, name='instructor-forum-thread'),
    path('instructor_invoice', views.instructor_invoice, name='instructor-invoice'),
    path('instructor_invoice_settings', views.instructor_invoice_settings, name='instructor-invoice-settings'),
    path('instructor_messages', views.instructor_messages, name='instructor-messages'),
    path('instructor_messages_2', views.instructor_messages_2, name='instructor-messages-2'),
    path('instructor_profile', views.instructor_profile, name='instructor-profile'),
    path('instructor_quiz_edit', views.instructor_quiz_edit, name='instructor-quiz-edit'),
    path('instructor_quiz_results', views.instructor_quiz_results, name='instructor-quiz-results'),
    path('instructor_quizzes', views.instructor_quizzes, name='instructor-quizzes'),
    path('instructor_take_course', views.instructor_take_course, name='instructor-take-course'),
    path('instructor_take_quiz', views.instructor_take_quiz, name='instructor-take-quiz'),
    path('instructor_view_course', views.instructor_view_course, name='instructor-view-course'),
    
]