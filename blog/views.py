from django.shortcuts import render_to_response
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render_to_response(request, 'blog/post_list.html', {'posts': posts})