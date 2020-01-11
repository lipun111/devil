from django.shortcuts import render
from django.views.generic import ListView
from users.models import Post
# Create your views here.


def home_view(request):
    post = Post.objects.all()
    context1={'post':post}
    return render(request, 'home/home_page.html', context1)


class PostListView(ListView):
    model = Post
    template_name = 'home/home_page.html'
    context_object_name = 'post'
    ordering = ['-date_published']
