from django.urls import path
from .views import ProfileView, ProjectView

urlpatterns = [
    path('about-me', ProfileView.as_view()),
    path('projects', ProjectView.as_view())
]
