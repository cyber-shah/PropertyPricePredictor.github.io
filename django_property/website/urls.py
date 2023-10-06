"""
Three step process to create a new page:

1. actual HTML page template (in templates folder)
2. URL configuration (that maps a URL to a view)
3. Create a view (a function that returns a rendered HTML page)
"""
from django.urls import path, include,
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
