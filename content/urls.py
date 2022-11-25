from django.urls import path

from . import views

urlpatterns = [
    path("contents/", views.ContentView.as_view()),
    path("contents/<int:content_id>/", views.ContentModifications.as_view()),
    path("contents/filter/", views.ContentParams.as_view())

]
