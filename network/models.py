from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.
class Profile(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phno = models.IntegerField(null=True)
    dob = models.DateField()
    sex = models.CharField(max_length= 10)
    bio = models.TextField(null=True)
    profile_pic = models.FileField(upload_to="static/profile",null=True,default="static/img/profile_pic.png")
    relationship_status = models.CharField(max_length = 35,null=True)
    profession = models.CharField(max_length= 100,null=True)
    profile_status = models.CharField(max_length = 15)
    validation_otp = models.CharField(max_length = 8,null=True)


    def __str__(self):
        return str(self.user_id) + ". " +self.name 


class Friend(models.Model):
    f_id = models.AutoField(primary_key = True)
    profile1 = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="f1")
    profile2 = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="f2")
    time_of_friendship = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.f_id)

class FriendRequest(models.Model):
    fr_id = models.AutoField(primary_key = True)
    profile1 = models.ForeignKey(Profile,related_name="fr1",on_delete=models.CASCADE) #requester
    profile2 = models.ForeignKey(Profile,related_name="fr2",on_delete=models.CASCADE) #receiver
    timestamp = models.DateField()
    receiver_seen = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.fr_id)

class Post(models.Model):
    post_id = models.AutoField(primary_key = True)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="user")
    media_type = models.CharField(max_length = 10)
    desc = models.CharField(max_length = 255,null=True)
    media = models.FileField(upload_to='static/posts',null=True)
    parent = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,related_name="parent")
    privacy = models.CharField(max_length = 15)
    no_of_likes = models.IntegerField(default = 0)
    no_of_comments = models.IntegerField(default = 0)
    timestamp = models.DateTimeField(null = True)
    
    def __str__(self):
        return str(self.post_id)

@receiver(pre_delete, sender=Post)
def File_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.media.delete(False)



class Comment(models.Model):
    c_id = models.AutoField(primary_key = True)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    desc = models.CharField(max_length =100)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self): return str(self.c_id)

class Like(models.Model):
    like_id = models.AutoField(primary_key = True)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str(self): return str(self.like_id)