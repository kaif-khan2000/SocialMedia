from django.contrib import admin
from .models import Profile,Friend,FriendRequest,Post,Comment,Like
# Register your models here.
admin.site.register(Profile)
admin.site.register(Friend)
admin.site.register(FriendRequest)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)

