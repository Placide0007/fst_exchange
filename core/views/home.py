from django.shortcuts import render
from django.core.paginator import Paginator
from ..models import Post

def home(request):
    posts = Post.objects.all().order_by("-created_at")

    paginator = Paginator(posts, 3)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'core/home.html', {
        'posts': page_obj
    })