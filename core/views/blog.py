from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.templatetags.static import static
from ..models import Post, Reaction, Comment, Category


@login_required
def blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        category_id = request.POST.get("category")

        Post.objects.create(
            title=title,
            content=content,
            category_id=category_id,
            user=request.user
        )

        return redirect("blog")

    categories = Category.objects.all()

    category_id = request.GET.get("category")
    search = request.GET.get("search")

    posts = Post.objects.all()

    if search:
        posts = posts.filter(title__icontains=search) | posts.filter(content__icontains=search)

    if category_id:
        posts = posts.filter(category_id=category_id)

    posts = posts.order_by("-created_at")

    return render(request, 'core/blog/blog.html', {'posts': posts, 'categories': categories})


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


@login_required
def comment_post(request, post_id):
    
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        
        content = request.POST.get("content", "").strip()

        if not content:
            messages.error(request, "Le commentaire ne peut pas être vide.")
        else:
            Comment.objects.create(
                content=content,
                user=request.user,
                post=post
            )

            messages.success(request, "Commentaire ajouté avec succès.")

    return redirect("show", id=post.id)