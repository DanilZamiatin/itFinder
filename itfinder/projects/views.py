from django.shortcuts import render


def projects(request):
    projectList = [{'id': '1',
                    'title': 'Online Cinema',
                    'description': 'Cinema with the Most Comprehensive Film Library'},
                   {'id': '2',
                    'title': 'IT-Source platform',
                    'description': 'Courses in Frontend, Backend, and Mobile Development.'},
                   {'id': '3',
                    'title': 'Recruiting Portal',
                    'description': 'Vacancies for top-class specialists.'},
                   ]
