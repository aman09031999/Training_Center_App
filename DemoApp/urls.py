from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<slug:course_slug>', views.course_details, name='course_details'),
]