#!/usr/bin/python
# -*- coding: utf-8 -*-
import django_filters
from django_filters import rest_framework as drf_filters

from .models import Video


class VideoFilter(drf_filters.FilterSet):
    creator_name = django_filters.CharFilter(field_name='creator__name')

    class Meta:
        model = Video
        fields = ['creator_name']
        # fields = ['publish_time']