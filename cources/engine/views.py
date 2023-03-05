from django.views import View
from django.shortcuts import render



# Create your views here.
class HomePage(View):
    def get(self, request):
        return render(request, 'engine/home.html')