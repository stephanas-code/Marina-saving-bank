from django.urls import re_path  as  url
from . import views

app_name = "profiles"

urlpatterns = [
    url(r"^account_status/$", views.index, name = "account_status"),
    url(r"^money_transfer/", views.money_transfer, name = "money_transfer"),
    url(r"^otherbank/$", views.otherbank, name = "otherbank"),
    url(r"^history/$", views.history, name = "history"),
    url(r"^billing/$", views.billing, name = "billing"),
    url(r"^online_pay/$", views.online_pay, name = "online_pay"),
    url(r"settings/$", views.settings, name = "settings"),
    url(r"edit_details/", views.edit_details, name = "edit_details"),
    url(r"delete_account/$", views.delete_account, name = "delete_account")
]
