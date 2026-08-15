from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.templatetags.static import static
from ..models import Post, Reaction


@login_required
def blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        Post.objects.create(
            title=title,
            content=content,
            user=request.user
        )

        return redirect("blog")

    posts = Post.objects.all().order_by("-created_at")

    return render(request, 'core/blog/blog.html', {'posts': posts})


@login_required
def show(request, id):
    post = get_object_or_404(Post, id=id)

    return render(request, 'core/blog/blog_show.html', {'post': post})


@login_required
def react_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    reaction = Reaction.objects.filter(
        user=request.user,
        post=post
    )

    if reaction.exists():
        reaction.delete()
        liked = False
    else:
        Reaction.objects.create(
            user=request.user,
            post=post
        )
        liked = True

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'liked': liked,
            'count': post.reactions.count(),
            'liked_icon_url': static('icons/like_full.svg'),
            'unliked_icon_url': static('icons/like.svg'),
        })

    return redirect("blog")