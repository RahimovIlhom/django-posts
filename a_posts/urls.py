from django.urls import path

from .views import home_view, post_create_view, post_delete_view, post_edit_view, post_detail_view, send_comment, \
    comment_delete_view, send_reply, reply_delete_view, post_like_view, comment_like_view, reply_like_view

urlpatterns = [
    path('', home_view, name='home'),
    path('category/<tag>/', home_view, name='category'),
    path('post/create/', post_create_view, name='post-create'),
    path('post/<str:post_id>/detail/', post_detail_view, name='post-detail'),
    path('post/<str:post_id>/edit/', post_edit_view, name='post-edit'),
    path('post/<str:post_id>/delete/', post_delete_view, name='post-delete'),
    path('post/<str:pk>/like/', post_like_view, name='like-post'),
    path('comment/send/<pk>/', send_comment, name='send-comment'),
    path('comment/<str:pk>/like/', comment_like_view, name='like-comment'),
    path('comment/<str:comment_id>/delete/', comment_delete_view, name='comment-delete'),
    path('reply/send/<pk>/', send_reply, name='send-reply'),
    path('reply/<str:pk>/like/', reply_like_view, name='like-reply'),
    path('reply/<str:reply_id>/delete/', reply_delete_view, name='reply-delete'),
]
