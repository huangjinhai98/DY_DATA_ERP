#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.urls import path
from .views import index

app_name = 'erp'
urlpatterns = [
    # path('api/index/', views.index),
    # path('api/index/', views.IndexVideoListAPIView.as_view()),
    path('api/index/', index),
]