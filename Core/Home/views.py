from rest_framework.decorators import api_view
from rest_framework.response import Response

from Home.serializers import *
from Home.models import *

@api_view(['GET' , 'POST'])
def index(request):
  personal_info = {
    "name":"Roman Humagain",
    "age":21,
    "Skills":["Java" , "Python" , "Django"] ,
    "course":"BSC Hons"
  }
  
  if request.method == 'GET':
    search = request.GET.get('search')
    print(search)
  
  if request.method == "POST":
    data = request.data
    print(data)
    
    return Response(data)
  
  return Response(personal_info)

@api_view(['GET' , 'POST' , 'PUT' , 'PATCH' , 'DELETE'])
def person(request):
  if request.method == "GET":
    person = Person.objects.all()
    serializer = PeopleSerializers(person , many = True)
    return Response(serializer.data)
  
  elif request.method == "POST":
    data = request.data
    serializer = PeopleSerializers(data=data )
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)
  
  elif request.method == 'PUT':
    data = request.data
    person = Person.objects.get(id = data['id'] )
  
    serializer = PeopleSerializers(person , data = data)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)

    return Response(serializer.errors)
  
  elif request.method == 'PATCH':
    data = request.data
    person = Person.objects.get(id = data['id'] )
  
    serializer = PeopleSerializers(person , data = data , partial =  True)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)

    return Response(serializer.errors)
  
  elif request.method == "DELETE":
    data = request.data
    person = Person.objects.get(id = data['id'])
    person.delete()
    return Response({'message':'Person Deleted'})
    