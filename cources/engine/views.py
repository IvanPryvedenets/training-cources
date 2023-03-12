from django.views import View
from .forms import *
from django.shortcuts import render



# Create your views here.
class HomePage(View):
    def get(self, request):
        return render(request, 'engine/home.html')

class AboutPage(View):
    def get(self, request):
        return render(request, 'engine/about.html')

class CoursesPage(View):
    def get(self, request):
        return render(request, 'engine/courses.html')

class StaffPage(View):
    def get(self, request):
        return render(request, 'engine/staff.html')

class BlogPage(View):
    def get(self, request):
        return render(request, 'engine/blog.html')

class ContactPage(View):
    def get(self, request):
        return render(request, 'engine/contact.html')

class SignInPage(View):
    def get(self, request):
        form = SignInForm()

        return render(request, 'engine/signin.html', context={form: 'form'})

class SignUpPage(View):
    def get(self, request):
        return render(request, 'engine/signup.html')
    
    def post(self, request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
        return render(request, 'engine/signup.html')