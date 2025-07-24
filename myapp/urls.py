from django.urls import path
from . import views


urlpatterns = [
    path('List/', views.TodoList, name="TodoList")
]
