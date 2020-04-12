from django.urls import path
from . import views

urlpatterns = [
    path('', views.fixed_instructor_dashboard, name='fixed-instructor-dashboard'),
    path('fixed_instructor_account_edit', views.fixed_instructor_account_edit, name='fixed-instructor-account-edit'),
    path('fixed_instructor_browse_courses', views.fixed_instructor_browse_courses, name='fixed-instructor-browse-courses'),
    path('fixed_instructor_carts', views.fixed_instructor_carts, name='fixed-instructor-cart'),
    path('fixed_instructor_course_edit', views.fixed_instructor_course_edit, name='fixed-instructor-course-edit'),
    path('fixed_instructor_courses', views.fixed_instructor_courses, name='fixed-instructor-courses'),
    path('fixed_instructor_earnings', views.fixed_instructor_earnings, name='fixed-instructor-earnings'),
    path('fixed_instructor_edit_invoice', views.fixed_instructor_edit_invoice, name='fixed-instructor-edit-invoice'),
    path('fixed_instructor_forum', views.fixed_instructor_forum, name='fixed-instructor-forum'),
    path('fixed_instructor_forum_ask', views.fixed_instructor_forum_ask, name='fixed-instructor-forum-ask'),
    path('fixed_instructor_forum_thread', views.fixed_instructor_forum_thread, name='fixed-instructor-forum-thread'),
    path('fixed_instructor_invoice', views.fixed_instructor_invoice, name='fixed-instructor-invoice'),
    path('fixed_instructor_invoice_settings', views.fixed_instructor_invoice_settings, name='fixed-instructor-invoice-settings'),
    path('fixed_instructor_messages', views.fixed_instructor_messages, name='fixed-instructor-messages'),
    path('fixed_instructor_messages_2', views.fixed_instructor_messages_2, name='fixed-instructor-messages-2'),
    path('fixed_instructor_profile', views.fixed_instructor_profile, name='fixed-instructor-profile'),
    path('fixed_instructor_quiz_edit', views.fixed_instructor_quiz_edit, name='fixed-instructor-quiz-edit'),
    path('fixed_instructor_quiz_results', views.fixed_instructor_quiz_results, name='fixed-instructor-quiz-results'),
    path('fixed_instructor_quizzes', views.fixed_instructor_quizzes, name='fixed-instructor-quizzes'),
    path('fixed_instructor_take_course', views.fixed_instructor_take_course, name='fixed-instructor-take-course'),
    path('fixed_instructor_take_quiz', views.fixed_instructor_take_quiz, name='fixed-instructor-take-quiz'),
    path('fixed_instructor_view_course', views.fixed_instructor_view_course, name='fixed-instructor-view-course'),
    
]