# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r"^login/$", auth_views.login, name="login"),
    url(
        r"^logout/$", auth_views.logout, {"next_page": "/login"}, name="logout"
    ),
    url(r"^admin/", admin.site.urls),
    url(r"^", include("core.urls")),
]
