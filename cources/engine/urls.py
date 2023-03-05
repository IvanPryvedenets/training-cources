from django.urls import path

from engine.views import *

urlpatterns = [
    path('', HomePage.as_view(), name='test'),
]