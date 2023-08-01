from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import *
from Home.serializers import PeopleSerializer

# Create your views here.

@api_view(['GET' , 'POST'])
def index(request):
  courses = {
      'course_name':'python',
      'learn':['django' , 'flask' ,'RestApi'],
      'course_provider':'Roman'
    }
  if request.method == "GET":
    search = request.GET.get('search')
    print(search)
    print("you hit a GET method")
    
  elif request.method == "POST":
    data  = request.data
    print(data['age'])
    
    print("you hit a POST method")
    
  elif request.method == "PUT":
    print("you hit a PUT method")
  
  return Response(courses)



@api_view(['GET' , 'POST' , 'PATCH' , 'PUT'])
def person(request):
  if request.method == 'GET':
    objs = Person.objects.all()
    serializer = PeopleSerializer(objs , many = True)
    return Response(serializer.data)
    
  elif request.method == 'POST':
    data = request.data
    serializer = PeopleSerializer(data=data)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    
    return Response(serializer.errors)
  
  elif request.method == 'PUT':
    data = request.data
    serializer = PeopleSerializer(data = data)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)

    return Response(serializer.errors)
  
  elif request.method == 'PATCH':
    data = request.data
    objs = Person.objects.get(id = data['id'])
    serializer = PeopleSerializer(objs,data = data , partial = True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)

  
