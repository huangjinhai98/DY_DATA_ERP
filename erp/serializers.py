#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Video, Creator, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'name',
            'pid',
        ]


class CreatorSerializer(serializers.ModelSerializer):
    tag = TagSerializer()
    class Meta:
        model = Creator
        fields = [
            'id',
            'name',
            'fans_count',
            'index_source',
            'intro',
            'image',
            'like_count',
            'video_count',
            'tag_id',
            'tag',
        ]


class VideoListSerializer(serializers.ModelSerializer):
    # creator = CreatorSerializer()
    creator = serializers.CharField(source='creator.name')

    class Meta:
        model = Video
        fields = [
            'id',
            'title',
            'source',
            'like_num',
            'comment_num',
            'share_num',
            'collect_num',
            'video_id',
            'publish_time',
            # 'creator_id',
            'creator',
        ]


class VideoRetrieveSerializer(serializers.ModelSerializer):
    creator = CreatorSerializer()
    # creator = serializers.CharField(source='creator.name')

    class Meta:
        model = Video
        fields = [
            'id',
            'title',
            'source',
            'like_num',
            'comment_num',
            'share_num',
            'collect_num',
            'video_id',
            'publish_time',
            # 'creator_id',
            'creator',
        ]