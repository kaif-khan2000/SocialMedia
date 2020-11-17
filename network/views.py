from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core import serializers
from django.contrib.auth import authenticate,login,logout
from .models import Profile,FriendRequest,Friend,Post,Comment,Like
from datetime import datetime
import json
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request,'landing/landing-page.html')
    email = request.user.username
    profile = Profile.objects.get(email = email)
    requests = FriendRequest.objects.filter(profile2 = profile).count()
    posts = Post.objects.all().order_by('-timestamp')
    params = {
        'profile':profile,
        'requests':requests,
        'posts':posts,
    }     
    return render(request,'home/home.html',params)

def register(request):
    if request.is_ajax and request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        dob = request.POST['dob']
        gender = request.POST['gender']

        data = {
            'status' : 'fail',
            'message' : '',
        }

        if name == "" or email=="" or password == "" or dob == "" or gender == "":
            data['message'] = 'Fields are empty'
            return JsonResponse(data,status=200)
        elif '@gitam.in' not in email:
            data['message'] = 'Need gitam mail to register'
            return JsonResponse(data,status=200)
        elif len(password)<8:
            data['message'] = 'passwords do not match'
            return JsonResponse(data,status=200)
        elif password != confirmPassword:
            data['message'] = 'passwords do not match'
            return JsonResponse(data,status=200)

        try:
            user = User.objects.create_user(email,email,password)
        except:
            data['message'] = 'email already exists.'
            return JsonResponse(data,status=200)
        
        profile = Profile.objects.create(name=name,email=email,dob= dob,sex=gender)
        user = authenticate(username=name,password=password)
        
        if user is not None:
            login(request,user)

        data['status'] = 'success'
        data['message'] = ''
        return JsonResponse(data,status=200)

def signIn(request):
      if request.is_ajax and request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        data = {
            'status':'fail',
            'message':''
        }

        user = authenticate(username=email,password=password)
        if user is not None:
            data['status'] = 'success'
            login(request,user)
        else:
            data['message'] = "Worng Credentials"

        return JsonResponse(data,status=200)

def logout_req(request):
    logout(request)
    return redirect('/')


def friendsList(request):
    if request.method == "GET":
        email = request.user.username
        profile = Profile.objects.get(email=email)

        friends = Friend.objects.filter(profile1 = profile)
        friends = friends.union(Friend.objects.filter(profile2=profile))
        actual_friends = Profile.objects.filter(user_id = '-1')
        for friend in friends:
            
            if friend.profile1 == profile:
                actual_friends = actual_friends.union(Profile.objects.filter(user_id = friend.profile2.user_id))
            else:
                actual_friends = actual_friends.union(Profile.objects.filter(user_id = friend.profile1.user_id))
        data = serializers.serialize('json',actual_friends)
        return HttpResponse(data,content_type='application/json')


def addPost(request):
    if request.method == "POST":
        text = request.POST.get('post_text')
        media_type = 'text'
        file1 = None
        try:
            file1 = request.FILES['video']
            media_type="video"
        except:
            try:
                file1 = request.FILES['img']
                media_type = "image"
            except:
                pass
        email = request.user.username
        profile = Profile.objects.get(email = email)
        Post.objects.create(
            user = profile,
            media_type = media_type,
            media = file1,
            desc = text,
            privacy = 'public',
            timestamp = datetime.now()
        )

        return redirect('/')

class CommentView():
    def __init__(self,u_id,name,profile_pic,comment,timeStamp):
        self.u_id = u_id
        self.name = name
        self.comment = comment
        self.timeStamp = str(timeStamp)
        self.profile_pic = profile_pic
        
def loadComments(request):
    if request.method == "GET":
        post_id = request.GET['id']
        post = Post.objects.get(post_id = post_id)
        comments = Comment.objects.filter(post = post).order_by('-timestamp')
        data = []
        for comment in comments:
            profile = Profile.objects.get(user_id = comment.user.user_id)
            data.append(CommentView(profile.user_id,profile.name,profile.profile_pic.name,comment.desc,comment.timestamp).__dict__)
            
        data = json.dumps(data)
        return HttpResponse(data,content_type='application/json')

def addComment(request):
    if request.method == "GET":
        post_id = request.GET['id']
        comment = request.GET['comment']
        post = Post.objects.get(post_id = post_id)
        email = request.user.username
        user = Profile.objects.get(email = email)

        Comment.objects.create(
            user = user,
            post = post,
            desc = comment,
        )

        return HttpResponse()

def addLike(request):
    if request.method == "GET" and request.is_ajax :
        post_id = request.GET.get('id')
        email = request.user.username
        post = Post.objects.get(post_id = post_id)
        profile = Profile.objects.get(email = email)
        Like.objects.create(
            user = profile,
            post = post
        )
        post.no_of_likes += 1
        post.save()
        data = {
            'no_of_likes': post.no_of_likes
        }

        return JsonResponse(data,status=200)

def removeLike(request):
    if request.method == "GET" and request.is_ajax :
        post_id = request.GET.get('id')
        email = request.user.username
        post = Post.objects.get(post_id = post_id)
        profile = Profile.objects.get(email = email)
        Like.objects.get(
            user = profile,
            post = post
        ).delete()
        post.no_of_likes -= 1
        post.save()
        data = {
            'no_of_likes': post.no_of_likes
        }

        return JsonResponse(data,status=200)


class PostView():
    def __init__(self,kid,name,timestamp,profile_pic,desc,media,media_type,no_of_likes,like):
        self.id = kid
        self.name = name
        self.timestamp = str(timestamp)
        self.profile_pic = profile_pic
        self.desc = desc
        self.media = media
        self.media_type = media_type
        self.no_of_likes = no_of_likes
        self.like = like

def fetchPost(request):
    if request.is_ajax and request.method == "GET":
        email = request.user.username
        profile = Profile.objects.get(email = email)
        friends = Friend.objects.filter(profile1 = profile)
        friends = friends.union(Friend.objects.filter(profile2 = profile))
        ids = []
        for friend in friends:
            if (friend.profile1 == profile):
                ids.append(friend.profile2.user_id)
            else:
                ids.append(friend.profile1.user_id)

        
        next_page = int(request.GET['next'])
        next_page = next_page*10

        posts = Post.objects.filter(user__user_id__in = ids).union(Post.objects.filter(user=profile)).order_by('-timestamp')[next_page:next_page+10]
        data = []
        for post in posts:
            like = True
            try:
                Like.objects.get(post = post,user=profile)
            except:
                like = False
            data.append(PostView(post.post_id,post.user.name,post.timestamp,post.user.profile_pic.name,post.desc,post.media.name,post.media_type,post.no_of_likes,like).__dict__)
        
        data = json.dumps(data)
        return HttpResponse(data,content_type='application/json')
        
