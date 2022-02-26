from multiprocessing import context
from django.shortcuts import render
from .models import Posts


def index(request):
    if request.method == "GET":
        context = {"posts": Posts.objects.all().order_by("-created_at")}
    else:
        post = Posts(title=request.POST["title"], body=request.POST["body"])
        post.save()
        context = {"posts": Posts.objects.all().order_by("-created_at")}
    return render(request, "index.html", context)

