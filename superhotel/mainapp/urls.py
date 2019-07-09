app_name='mainapp'

from django.urls import path
from django.urls import re_path
import mainapp.views as mainapp

urlpatterns = [
    path('booking/', mainapp.dataFromInputBooking, name='dataFromInputBooking'),
    path('book_a_room/', mainapp.dataFromInputBookARoom, name='dataFromInputBookARoom'),
]