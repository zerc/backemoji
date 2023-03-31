from django.urls import path

from .views import show_feedback, success

urlpatterns = [
    path("<slug:slug>/", show_feedback, name="show_feedback"),
    path("<slug:slug>/success", success, name="success"),
]
