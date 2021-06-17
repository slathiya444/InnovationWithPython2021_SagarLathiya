from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm

# Create your views here.



# @login_required(login_url = 'login')
def function(request):
    post = Post.objects.all()
    context = {
        'posts': post
    }
    return render(request,'home.html', context)

def fun2(request):
    return render(request,'about.html')

def createPost(request):
    form = PostForm(initial = {'author' : request.user})
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            form = PostForm()

    context = {'form': form}

    return render (request,'createPost.html', context)

def updatePost(request, _id):
    postid = Post.objects.get(id=_id)
    form = PostForm(instance = postid)
    if request.method == "POST":
        form = PostForm(request.POST, instance=postid)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}

    return render (request,'createPost.html', context)

def myPost(request,_id):
    user = User.objects.get(id=_id)
    post = user.post_set.all()
    context = {'user' : user, 'post': post}
    return render(request,'mypost.html',context)

def delete(request,_id):
    post = Post.objects.get(id=_id)
    if request.method == "POST":
        # form = PostForm(request.POST, instance=postid)
        post.delete()
        return redirect('home')

    context = {'post' :post}

    return render(request,'createPost.html', context)




