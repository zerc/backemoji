from django.urls import path

from .views import show_feedback

urlpatterns = [
    path("<slug:slug>/", show_feedback),
]
