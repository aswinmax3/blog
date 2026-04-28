from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('new_blog/', views.BlogCreateView.as_view(), name='new_blog'),
    path('new_post/', views.PostCreateView.as_view(), name='new_post'),
    path('edit_post/<int:pk>/', views.PostUpdateView.as_view(), name='edit_post'),
]