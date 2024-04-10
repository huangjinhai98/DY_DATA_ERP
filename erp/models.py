from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)
    pid = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField()


class Creator(models.Model):
    name = models.CharField(max_length=255)
    author_id = models.CharField(max_length=20)
    tag = models.ForeignKey('Tag', on_delete=models.SET_NULL, null=True)
    # tag_id = models.IntegerField()
    fans_count = models.IntegerField()
    index_source = models.CharField(max_length=255)
    intro = models.TextField()
    image = models.CharField(max_length=255)
    sex = models.BooleanField
    like_count = models.IntegerField()
    video_count = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField()


class Video(models.Model):
    creator = models.ForeignKey('Creator', on_delete=models.SET_NULL, null=True)
    # creator_id = models.IntegerField()
    title = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    like_num = models.IntegerField()
    comment_num = models.IntegerField()
    share_num = models.IntegerField()
    collect_num = models.IntegerField()
    video_id = models.CharField(max_length=255)
    publish_time = models.CharField(max_length=255)
    create_time = models.IntegerField()
    update_time = models.IntegerField()
