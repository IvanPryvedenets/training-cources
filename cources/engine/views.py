from django.views import View
from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
class HomePage(View):
    def get(self, request):
        return HttpResponse('hello world')