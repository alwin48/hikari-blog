from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('posts/', views.BlogPostListView.as_view(), name = 'posts'),
    path('post/<int:pk>', views.BlogPostDetailView.as_view(), name = 'post-detail'),
    path('post/create_post', views.create_post, name='create_post'),
]