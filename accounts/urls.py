from django.urls import re_path as url
from . import views

app_name = "accounts"

urlpatterns = [
    url(r"^register/$", views.register, name = "signup"),
    url(r"^login/$", views.sign_in, name = "signin"),
    url(r"^logout/$", views.logout_view, name = "logout"),
]
