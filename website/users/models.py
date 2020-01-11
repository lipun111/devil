from django.db import models

# Create your models here.

class Post(models.Model):
    user_name = models.CharField(max_length=200, null=False)
    post_title = models.CharField(max_length=200, null=False)
    post_content = models.TextField()
    date_published = models.DateField(blank=True, null=False)
    user_profile_link = models.URLField(blank=True, null=False)

    def __str__(self):
        return self.user_name
