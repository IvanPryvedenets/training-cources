from django.urls import path

from engine.views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about/', AboutPage.as_view(), name='about'),
    path('courses/', CoursesPage.as_view(), name='courses'),
    path('staff/', StaffPage.as_view(), name='staff'),
    path('blog/', BlogPage.as_view(), name='blog'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('signin/', SignInPage.as_view(), name='signin'),
    path('signup/', SignUpPage.as_view(), name='signup'),
    path('student/', StudentPage.as_view(), name='student'),
    path('teacher/', TeacherPage.as_view(), name='teacher'),
]