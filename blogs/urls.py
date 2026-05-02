from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.home, name='home'),
    path('new-blog/', views.new_blog, name='new_blog'),
    path('new-post/', views.new_post, name='new_post'),
    path('analytics/', views.analytics, name='analytics'),
    path('settings/', views.settings_view, name='settings'),
    path('profile/', views.profile, name='profile'),
    path('messages/', views.messages_view, name='messages'),
    path('notifications/', views.notifications, name='notifications'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    
     path('new_post/', views.new_post, name='new_post'),

    path('views/', views.total_views, name='total_views'),
    path('likes/', views.total_likes, name='total_likes'),
    
        path('analytics/', views.analytics, name='analytics'),

    # 👉 NEW BUTTON LINKS
    path('profile/', views.profile, name='profile'),
    path('notifications/', views.notifications, name='notifications'),
    path('new_post/', views.new_post, name='new_post'),
    path('analytics/views/', views.activity_views, name='activity_views'),
    path('analytics/likes/', views.activity_likes, name='activity_likes'),
    path('analytics/', views.analytics, name='analytics'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
]