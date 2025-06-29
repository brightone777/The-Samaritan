import os
import logging
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib.admin.views.decorators import staff_member_required
from .models import Post
from .forms import PostForm

logger = logging.getLogger(__name__)

# Helper function to get client IP address


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')


# Homepage - show all unblocked posts and allow anonymous posting
def home(request):
    posts = Post.objects.filter(blocked=False).order_by('-created_at')
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            if request.FILES.get('image'):
                from django.core.files.storage import default_storage
                logger.info("Image upload detected.")
                logger.info("Storage backend: %s", default_storage)
                logger.info("Uploaded file name: %s",
                            request.FILES['image'].name)

            post = form.save(commit=False)
            post.user = request.user if request.user.is_authenticated else None
            post.ip_address = get_client_ip(request)
            post.save()
            return redirect('home')

    return render(request, 'posts/all_posts.html', {'posts': posts, 'form': form})


# Optional separate anonymous post creation page
def create_anonymous_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            if request.FILES.get('image'):
                from django.core.files.storage import default_storage
                logger.info("Image upload detected.")
                logger.info("Storage backend: %s", default_storage)
                logger.info("Uploaded file name: %s",
                            request.FILES['image'].name)

            post = form.save(commit=False)
            post.user = request.user if request.user.is_authenticated else None
            post.ip_address = get_client_ip(request)
            post.save()
            return redirect('post_success')
    else:
        form = PostForm()

    return render(request, 'posts/create_anonymous_post.html', {'form': form})


# Success page after posting
def post_success(request):
    return render(request, 'posts/post_success.html')


# Post list view for admin and public users
def post_list(request):
    if request.user.is_staff:
        posts = Post.objects.all().order_by('-created_at')
    else:
        posts = Post.objects.filter(blocked=False).order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})


# Admin: block or unblock a post
@require_POST
@staff_member_required
def toggle_block(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.blocked = not post.blocked
    post.save()
    return HttpResponseRedirect(reverse('post_list'))


# Admin: delete a post
@require_POST
@staff_member_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('post_list'))


# Check if Cloudinary settings are loaded correctly (for debugging)
def test_cloudinary_config(request):
    return JsonResponse({
        "CLOUD_NAME": os.environ.get("CLOUDINARY_CLOUD_NAME"),
        "API_KEY": os.environ.get("CLOUDINARY_API_KEY"),
        "API_SECRET": os.environ.get("CLOUDINARY_API_SECRET"),
    })
