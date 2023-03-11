from django.views import View
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