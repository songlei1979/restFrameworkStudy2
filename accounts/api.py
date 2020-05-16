from accounts.models import Student, Subject, StudentSubject
from rest_framework import viewsets, permissions
from .serializers import StudentSerializer, SubjectSerializer, StudentSubjectSerializer


# Student Viewset
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentSerializer


# Subject Viewset
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubjectSerializer


# StudentSubject Viewset
class StudentSubjectViewSet(viewsets.ModelViewSet):
    queryset = StudentSubject.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentSubjectSerializer