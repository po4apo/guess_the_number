from django.urls import path
from .views import show_input_two_number

urlpatterns = [
    path('', show_input_two_number)
]