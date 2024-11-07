from django.urls import path
from .views import *

urlpatterns = [
    path('card', CardView.as_view()),
]