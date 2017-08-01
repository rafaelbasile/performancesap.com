from django.conf.urls import url, include
from django.contrib import admin
from .views import CoreViews

urlpatterns = [
    url(r'^$', CoreViews.as_view()),
]
