from django.urls import path
from TutorSystem import views

urlpatterns = [
    path('Variablen/', views.lesson_2_variables, name='lesson_2_variables'),
    path('Variablen_Aufgabe/', views.lesson_2_variables_exercise, name='lesson_2_variables_exercise'),
    path('Bedingte_Anweisungen_if/', views.lesson_2_conditional_statements_if,
         name='lesson_2_conditional_statements_if'),
    path('Turtle_Graphics/', views.lesson_2_turtle_graphics, name='lesson_2_turtle_graphics'),
]
