from django.urls import path
from projects import views
from ..views import projects
from ..views import project

urlpatterns = [

    path('', views.projects, name="projects"),
    path('project-object/<uuid:pk>/', views.project, name="project"),

]
