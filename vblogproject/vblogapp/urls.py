from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create_blog_view, name='create_blog'),
    path('blog/<int:blog_id>/', views.view_blog_view, name='view_blog'),
    path('blog/<int:blog_id>/comment/', views.add_comment_view, name='add_comment'),
    path('', views.home_view, name='home'),
]
