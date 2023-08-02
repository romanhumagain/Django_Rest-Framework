from rest_framework import serializers

from . models import *

class PeopleSerializers(serializers.ModelSerializer):
  
  class Meta:
    model = Person
    fields = "__all__"
    
    # to validate the age
  def validate(self, data):
    special_character = "~!@#$%^*&^()"
    for character in data['name']:
      if character in special_character:
        raise serializers.ValidationError("Name shouldn't contain any special character")
    
    if data['age']<18:
      raise serializers.ValidationError("Age should be greater than 18")
    return data
      