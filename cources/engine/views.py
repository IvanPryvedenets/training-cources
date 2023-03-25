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
            form = UserForm(request.POST)
            if form.is_valid():
                if form.data['person'] == 'student':
                    student = form.save()
                    return render(request, 'engine/student.html', context={'student': student})
                elif form.data['person'] == 'teacher':
                    teacher = Teacher.objects.create(
                        name=form.cleaned_data['name'],
                        last_name=form.cleaned_data['last_name'],
                        email=form.cleaned_data['email'],
                        password=form.cleaned_data['password'],
                        person=form.cleaned_data['person'],
                        school=request.POST.get('school'),
                        course1=request.POST.get('courses'),
                        sertificate=request.POST.get('sertificate1'),
                        sertificate1=request.POST.get('sertificate2'),
                    )
                    print(teacher)
                    return render(request, 'engine/teacher.html', context={'teacher': teacher})

            else:
                print(form.data)
                print(form.errors)

                return render(request, 'engine/signup.html')
                
        else:
            return render(request, 'engine/signup.html')

class StudentPage(View):
    def get(self, request):
        student = Student.objects.first()
        print(student.name)
        return render(request, 'engine/student.html', context={'student': student})

class TeacherPage(View):
    def get(self, request):
        student = Teacher.objects.first()
        print(teahcer.name)
        return render(request, 'engine/teacher.html', context={'teacher': teacher})
