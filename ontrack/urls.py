from django.urls import path

from . import views

app_name = "ontrack"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:unit_id>/", views.submissions, name="submissions"),
]