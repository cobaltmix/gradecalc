from django.urls import path
from . import views

urlpatterns = [
    path('calculate-grade/', views.calculate_grade, name='calculate_grade'),
    path('calculate-exam/', views.calculate_exam_score, name='calculate_exam'),
]
