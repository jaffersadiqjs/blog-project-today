from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView, add_comment, delete_comment,
    register_view
)
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<slug:slug>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('post/<slug:slug>/comment/', add_comment, name='add-comment'),
    path('comment/<int:pk>/delete/', delete_comment, name='delete-comment'),

    # auth
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
