from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
     path('', views.index, name='posts'),
     path('groups/', views.group_list, name='posts_list'),
     path('groups/<slug:slug>', views.group_posts, name='post_detail')
]
