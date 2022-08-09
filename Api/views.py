from ast import Return
import io
import json
from unicodedata import name
from urllib import response
from webbrowser import get
from django.shortcuts import render
from .models import Student, Section
from .serializer import StudentSerializer, SectionSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response







# Create your views here.
# def student_detail(request,pk):
#     stu = Student.objects.get(id = pk)
#     print(stu)
#     serializer = StudentSerializer(stu)
#     print("--------------------------------")
#     print(serializer.data)
#     print("--------------------------------")
    
#     # json_data =JSONRenderer().render(serializer.data)
#     # print(json_data)
#     # return HttpResponse(json_data, content_type='application/json')
#     return JsonResponse(serializer.data)

class student_create(APIView):
    def post(self, request,*args, **kwargs):
        try:
            Student.objects.create(
                name = request.POST.get('name'),
                roll = request.POST.get('roll'),
                city = request.POST.get('city'),
                ) 
            context = {
                    "status":status.HTTP_201_CREATED,
                    "success":True,
                    "response":"Successfully Created!"
                }               
                
            return JsonResponse(context,status=status.HTTP_201_CREATED)
            
        except Exception as excecption:
            context = {
                    "status":status.HTTP_400_BAD_REQUEST,
                    "success":False,
                    "response":str(excecption)
                }               
                
            return JsonResponse(context,status=status.HTTP_400_BAD_REQUEST)
        
   
        
class show(APIView):    
    def get(self, request ,pk ,*args, **kwargs,):
        print(pk)   
        try:
            get_data = Student.objects.get(id=pk)
            real_data = StudentSerializer(get_data)
            context = {
                "status":status.HTTP_200_OK,
                "success": True,
                "response": real_data.data
            }
            return Response(context,status=status.HTTP_200_OK)
        
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request,pk, *args, **kwargs):
       
            stu_obj = Student.objects.get(id = pk)
            print(stu_obj)
            data = request.data
            stu_obj.name = data["name"]
            stu_obj.roll = data["roll"]
            print(stu_obj.roll)
            print("----------------------------------")
            
            stu_obj.city = data["city"]
            
            stu_obj.save()
            
            getdata = StudentSerializer(stu_obj)
            print(getdata)

            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "response":getdata.data
            }
            return Response(context, status=status.HTTP_200_OK)
        
        
                        
        
        
        
        
class section_addApi(APIView):
    def post(self, request,*args, **kwargs):
        try:
            get_student=request.POST.get('student')
            get_section=request.POST.get('section')
            get_student_instance = Student.objects.get(name = get_student)
            
            Section.objects.create(student_id=get_student_instance.id,section=get_section)
            
            context = {
                "status":status.HTTP_201_CREATED,
                "sucess":True,
                "response":"Succefully Created"
            }  
            
            return Response(context, status=status.HTTP_201_CREATED)
        
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success": False,
                "response":str(exception)
                }
             
            return Response(context, status=status.HTTP_400_BAD_REQUEST )
        
        
class show_sectionApi(APIView):
    def get(self, request, id,  *args, **kwargs ):
        try:
            get_data = Section.objects.get(id = id)
            name_data = get_data.student
            print("================================================================")
            print(type(name_data))
            json_data = SectionSerializer(get_data)
            print(json_data.data)
            
            context = {
            "status":status.HTTP_200_OK,
            "status":True,
            "response":json_data.data,
            }            
            
            return Response(context, status.HTTP_200_OK)  

        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
                
            }    
        
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    
    
    
class update_studentAPI(APIView):
    pass
    
    
    