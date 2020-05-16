from rest_framework import serializers
from accounts.models import Student, Subject, StudentSubject


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class StudentSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSubject
        fields = '__all__'
