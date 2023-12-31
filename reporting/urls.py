from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("project/<str:pk>/", views.project, name='project'),
    path("login/", views.login, name='login'),
]