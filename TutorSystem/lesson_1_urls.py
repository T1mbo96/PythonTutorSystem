from django.urls import path
from TutorSystem import views

urlpatterns = [
    path('Blockly_Maze_Embedded/', views.test_blockly_maze_embed, name='test_blockly_maze_embed'),
    path('Blockly_Custom/', views.test_blockly_custom, name='test_blockly_custom'),
]
