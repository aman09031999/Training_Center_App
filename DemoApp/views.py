from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
# Create your views here.


def course_list(request):
    course = Course.objects.all()
    return render(request, "course/course_list.html",  {'course': course})


def course_details(request, course_slug):
    #   fetching

    return render(request, "course/course_details.html",)