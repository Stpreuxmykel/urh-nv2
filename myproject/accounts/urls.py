from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path("signup/", views.signup, name="signup"),
    path("add_student/", views.add_student, name="add_student"),
    path('update_student/<int:id>/', views.update_student, name='update_student'),
    path("delete_student/<int:id>/", views.delete_student, name="delete")
]