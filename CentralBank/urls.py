from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from django.conf.urls import include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import (handler400, handler403, handler404, handler500)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name = "home"),
    url(r'^markets', views.markets, name = "markets"),
    url(r'^about', views.about, name = "about"), 
    url(r'^blog', views.blog, name = "blog"),
    url(r'^partners', views.partners, name = "partners"),
    url(r'^legal', views.legal, name = "legal"),
    url(r'^contact', views.contact, name = "contact"),
    url(r'^accounts/', include("accounts.urls")),
    url(r'^profile/', include("profiles.urls")),
    url(r'^admins/', include("admins.urls"))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = 'profiles.views.delete_account'

#Change Site Title, Index Title and Site Title
admin.site.site_header = "Central Bank Administration"
admin.site.site_title = "Central Bank Administration"
admin.site.index_title = "Welcome to Central Bank Administration Admin Panel"
