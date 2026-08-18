from django.urls import path
from . import views

app_name = "academy"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("courses/", views.courses, name="courses"),
    path("courses/java/", views.java_course, name="java"),
    path("courses/python/", views.python_course, name="python"),
    path("events/", views.events, name="events"),
    path("benefits/", views.benefits, name="benefits"),
    path("contact/", views.contact, name="contact"),
    path("python-full-stack/", views.python_fullstack, name="python_fullstack"),
]


