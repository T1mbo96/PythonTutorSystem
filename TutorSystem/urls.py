from django.urls import path, include
from TutorSystem import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Sign_Up/', views.sign_up, name='sign_up'),
    path('Lesson_1/', include('TutorSystem.lesson_1_urls')),
    path('Lesson2/', include('TutorSystem.lesson_2_urls')),
    path('Kompendium/', views.syntax_compendium, name='compendium'),
]
