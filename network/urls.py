from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path('signIn',views.signIn,name="signIn"),
    path('logout',views.logout_req,name='logout'),
    path('friendsList',views.friendsList,name='friendsList'),
    path('addPost',views.addPost,name='addPost'),
    path('loadComments',views.loadComments,name='loadComments'),
    path('addComment',views.addComment,name='addComment'),
    path('addLike',views.addLike,name='addLike'),
    path('removeLike',views.removeLike,name='removeLike'),
    path('fetchPost',views.fetchPost,name='fetchPost'),
]