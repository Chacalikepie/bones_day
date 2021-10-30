from django.urls import path
from . import views

app_name = "bonesday"
urlpatterns = [
	path("", views.index, name="index"),
	path("bones", views.bones, name="bones")
]

