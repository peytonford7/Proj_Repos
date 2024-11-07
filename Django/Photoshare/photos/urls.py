from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_gallery, name='photo_gallery'),
    path('photo/<str:pk>/', views.photo_detail, name='photo_detail'),
    path('upload/', views.photo_upload, name='photo_upload'),
]
