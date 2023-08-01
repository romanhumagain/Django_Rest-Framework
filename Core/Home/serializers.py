from rest_framework import serializers

from . models import *
class PeopleSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Person
    
    # fields = ['name' , 'age']
    # exclude = ['name']    # to exclude the data
    fields = "__all__"    # to get the all fields
    

    