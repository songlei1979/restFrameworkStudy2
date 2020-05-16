from django.db import models


# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    birthdate = models.DateField()
    sex = models.CharField(max_length=100)
    programme = models.CharField(max_length=100)
    resident_status = models.CharField(max_length=100)
    resident_desc = models.CharField(max_length=100)
    ethnic_code = models.CharField(max_length=100)
    ethnic_desc = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Subject(models.Model):
    subject = models.CharField(max_length=100)


class StudentSubject(models.Model):
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    subjectid = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_nbr = models.CharField(max_length=100)
