from django.urls import path
from . import views

# new list called url patterns
urlpatterns = [
    # empty means root url
    # what happens when someone visits this url ? views.index
    # index is a function inside views
    # advisable to name it as the same function
    path('', views.index, name = 'index')
]


