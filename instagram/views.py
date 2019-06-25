from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from . models import Image,Profile,Comment
from django.contrib.auth.decorators import login_required
from .forms import NewProfileForm,NewPostForm,CommentForm
from django.contrib.auth.models import User



@login_required(login_url='/accounts/login/')
def welcome(request):
    
    images = Image.objects.all()
    
    profile = Profile.objects.all()
    
    return render(request,'index.html',{"images":images,"profile":profile})
def search_results(request):
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_profiles = User.objects.filter(username__icontains=search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message, "user":searched_profiles})
    else:
        message = "You haven't searched for any term."
        return render(request, 'search.html', {"message":message})  
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile=current_user
            post.save()
        return redirect('welcome')

    else:
        form = NewPostForm()
    return render(request, 'new-post.html', {"form": form})

@login_required(login_url='/accounts/login/')      
def new_profile(request,id):
    user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
        return redirect('profile')
    else:
        form = NewProfileForm()
    return render(request, 'new-profile.html', {"form":form,"user":user})

def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    posts=Image.objects.filter(profile_id=current_user.id)
    return render(request, 'profile-page.html',{"profile":profile,"posts":posts})
@login_required(login_url='/accounts/login/')   

def comment(request, id):
   current_user = request.user
   comments = Comment.objects.filter(image_id=id)
   profile = Profile.objects.all()
   image = Image.objects.get(id=id)
   if request.method == 'POST':
       form = CommentForm(request.POST, request.FILES)
       if form.is_valid():
           comment = form.save(commit=False)
           comment.image = image
           comment.username = current_user
           comment.name_id = current_user.id
           comment.save()
       return redirect('welcome')

   else:
       form = CommentForm()
   return render(request, 'comment.html', {'image': image, 'comments': comments, 'form': form, "user":current_user, "profile":profile})