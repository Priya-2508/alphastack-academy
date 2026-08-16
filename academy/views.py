from django.shortcuts import render

def home(request):
    return render(request, "academy/home.html")

def about(request):
    return render(request, "academy/about.html")

def courses(request):
    return render(request, "academy/courses.html")

def java_course(request):
    return render(request, "academy/java.html")

def python_course(request):
    return render(request, "academy/python.html")

def events(request):
    return render(request, "academy/events.html")

def benefits(request):
    return render(request, "academy/benefits.html")

def contact(request):
    return render(request, "academy/contact.html")

def python_fullstack(request):
    return render(request, "academy/python_fullstack.html")
