
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root view showing posts + form
    path('create/', views.create_anonymous_post, name='create_post'),
    path('success/', views.post_success, name='post_success'),
    path('posts/', views.post_list, name='post_list'),

    # Admin-only actions
    path('posts/<int:post_id>/block/', views.toggle_block, name='toggle_block'),
    path('posts/<int:post_id>/delete/', views.delete_post, name='delete_post'),
]
