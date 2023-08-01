from Home.views import *

from django.urls import path 

urlpatterns = [
  path('index/' , index , name='index'),
  path('person/' , person , name='person'),
]