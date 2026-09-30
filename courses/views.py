from django.shortcuts import render, get_object_or_404
from .models import Course


def home(request):
    search_query = request.GET.get("search", "")

    if search_query:
        courses = Course.objects.filter(title__icontains=search_query)
    else:
        courses = Course.objects.all()

    return render(
        request,
        "courses/home.html",
        {
            "courses": courses,
            "search_query": search_query,
        },
    )


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    return render(
        request,
        "courses/course_detail.html",
        {"course": course},
    )