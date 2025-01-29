from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostCreateForm, PostEditForm, CommentCreateForm, ReplyCreateForm
from .models import Post, Tag, Comment, Reply
from .utils import fetch_flickr_data


def home_view(request, tag=None):
    if tag:
        posts = Post.objects.filter(tags__slug=tag)
        tag = get_object_or_404(Tag, slug=tag)
    else:
        posts = Post.objects.all()

    categories = Tag.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
        'tag': tag
    }
    return render(request, template_name='a_posts/home.html', context=context)


@login_required
def post_create_view(request):
    post_form = PostCreateForm(request.POST or None)

    if request.method == 'POST' and post_form.is_valid():
        url = post_form.cleaned_data.get('url')
        test_url = url.replace("https://www.", "").replace("https://", "")

        if not test_url.startswith("flic.kr") and not test_url.startswith("flickr.com"):
            messages.error(request, "Please enter a valid Flickr URL.")
            return render(request, 'a_posts/post_create.html', {'post_form': post_form})

        flickr_data = fetch_flickr_data(url)

        if flickr_data['ok']:
            post = post_form.save(commit=False)
            post.image = flickr_data['data']['image']
            post.title = flickr_data['data']['title']
            post.artist = flickr_data['data']['artist']

            post.author = request.user

            post.save()
            post_form.save_m2m()
            return redirect('home')
        else:
            messages.error(request, flickr_data['data'])
    elif request.method == 'POST':
        messages.error(request, 'The form data is invalid.')

    return render(request, 'a_posts/post_create.html', {'post_form': post_form})


@login_required
def post_delete_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        messages.error(request, "Forbidden")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'The post has been deleted.')
        return redirect('home')

    return render(request, 'a_posts/post_delete.html', {'post': post})


@login_required
def post_edit_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        messages.error(request, "Forbidden")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    form = PostEditForm(instance=post)

    if request.method == 'POST':
        form = PostEditForm(instance=post, data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated.')
        else:
            messages.error(request, 'The form data is invalid.')

    context = {
        'post': post,
        'form': form
    }

    return render(request, 'a_posts/post_edit.html', context=context)


def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    comment_form = CommentCreateForm()
    reply_form = ReplyCreateForm()
    categories = Tag.objects.all()

    context = {
        'post': post,
        'comment_form': comment_form,
        'reply_form': reply_form,
        'categories': categories
    }

    return render(request, 'a_posts/post_detail.html', context)


@login_required
def post_like_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def send_comment(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.parent_post = post
            comment.save()

    return redirect('post-detail', post.id)


@login_required
def comment_like_view(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def send_reply(request, pk):
    comment = get_object_or_404(Comment, id=pk)

    if request.method == 'POST':
        form = ReplyCreateForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = request.user
            reply.parent_comment = comment
            reply.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def reply_like_view(request, reply_id):
    reply = get_object_or_404(Reply, pk=reply_id)

    if request.user in reply.likes.all():
        reply.likes.remove(request.user)
    else:
        reply.likes.add(request.user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def comment_delete_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author != request.user:
        messages.error(request, "Forbidden")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'The comment has been deleted.')
        return redirect('post-detail', comment.parent_post.id)

    return render(request, 'a_posts/comment_delete.html', {'comment': comment})


@login_required
def reply_delete_view(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)

    if reply.author != request.user:
        messages.error(request, "Forbidden")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    if request.method == 'POST':
        reply.delete()
        messages.success(request, 'The reply has been deleted.')
        return redirect('post-detail', reply.parent_comment.parent_post.id)

    return render(request, 'a_posts/reply_delete.html', {'reply': reply})
