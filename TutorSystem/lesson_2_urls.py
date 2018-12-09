from django.urls import path
from TutorSystem import views

urlpatterns = [
    path('Skulpt/', views.test_skulpt, name='test_skulpt'),
]
