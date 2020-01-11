from django.shortcuts import render
from users.models import Post
from api.serializers import PostSerializers
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
