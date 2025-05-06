from django.shortcuts import render

from django.http import JsonResponse
from .models import Post

def post_list(request):
    posts = Post.objects.all().values('title', 'description', 'date')
    return JsonResponse(list(posts), safe=False)
