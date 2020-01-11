from users.models import Post
from rest_framework.serializers import ModelSerializer

class PostSerializers(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
