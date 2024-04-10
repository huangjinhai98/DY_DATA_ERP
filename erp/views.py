from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend

from .models import Video, Creator
from .serializers import VideoListSerializer, CreatorSerializer, VideoRetrieveSerializer
from .filters import VideoFilter


# api装饰器
# @api_view(http_method_names=["GET"])
# def index(request):
#     # author_list = Creator.objects.all().order_by('-create_time')
#     # serializer = CreatorSerializer(author_list, many=True)
#     video_list = Video.objects.all().order_by('-create_time')
#     serializer = VideoListSerializer(video_list, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

# 基本的视图类
# class IndexVideoListAPIView(ListAPIView):
#     serializer_class = VideoListSerializer
#     queryset = Video.objects.all()
#     pagination_class = PageNumberPagination
#     permission_classes = [AllowAny]

# 首页视图集
class VideoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = VideoListSerializer
    queryset = Video.objects.all().order_by('creator')
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]

    serializer_class_table = {
        'list': VideoListSerializer,
        'retrieve': VideoRetrieveSerializer,
    }
    
    def get_serializer_class(self):
        return self.serializer_class_table.get(
            self.action, super(VideoViewSet, self).get_serializer_class()
        )

    filter_backends = [DjangoFilterBackend]
    filterset_class = VideoFilter


index = VideoViewSet.as_view({'get': 'list'})


# 对标选题库