from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Sign_Up/', views.sign_up, name='sign_up'),
    path('Lesson_1/', views.lesson_1, name='lesson_1'),
]
