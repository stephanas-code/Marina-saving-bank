from django.urls import re_path as url
from . import views

app_name = "admins"

urlpatterns = [
    url(r"^$", views.index, name = "admin_index"),
]
