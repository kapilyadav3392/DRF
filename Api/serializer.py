from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Student, Section

class StudentSerializer(serializers.ModelSerializer):
   class Meta:
       model = Student
       fields = '__all__'
    
class SectionSerializer(serializers.ModelSerializer):
    # name = serializers.SerializerMethodField() 
    class Meta:
        model = Section
        fields = ['id','student_name', 'section']
    
    # def get_name(self,obj):
    #     return obj.student.name