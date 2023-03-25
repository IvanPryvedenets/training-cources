from django.db import models

# Create your models here.
class Student(models.Model):
    avatar = models.ImageField(blank=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    person = models.CharField(max_length=50)

class Teacher(models.Model):
    avatar = models.ImageField(blank=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    person = models.CharField(max_length=50)
    school = models.CharField(max_length=100)
    course1 = models.CharField(max_length=100, blank=True)
    course2 = models.CharField(max_length=100, blank=True)
    sertificate = models.ImageField()
    sertificate1 = models.ImageField(blank=True)
    sertificate2 = models.ImageField(blank=True)

class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, blank=True)
    image = models.ImageField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    places = models.CharField(max_length=3)
    price = models.FloatField()
    terms = models.CharField(max_length=10)
    data = models.DateField()
