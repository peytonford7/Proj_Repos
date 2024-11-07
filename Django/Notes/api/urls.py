from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('notes/', views.getNotes, name="notes"),
    path('notes/<int:pk>/', views.getNote, name="note-list"),
    path('todo/', views.getTodos, name="todos"),
    path('todo/<int:pk>/', views.getTodo, name="todo-list"),

]