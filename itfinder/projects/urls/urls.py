from django.urls import path
from projects import views
from projects.views import projects
from projects.views import project

urlpatterns = [

    path('', views.projects, name="projects"),
    path('project-object/<int:pk>/', views.project, name="project"),

]
