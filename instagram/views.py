from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from . models import Image,Profile
from django.contrib.auth.decorators import login_required
from .forms import NewsProfileForm,NewPostForm
from django.contrib.auth.models import User



@login_required(login_url='/accounts/login/')
def welcome(request):
    images = Image.objects.all()
    
    return render(request,'index.html',{"images":images})
def search_results(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = User.objects.filter(username__icontains=search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message, "profile":searched_profiles})
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
    return render(request, 'new-article.html', {"form": form})

      
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewsProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.user_id=current_user.id
            profile.save()
        return redirect('profile')
    else:
        form = NewsProfileForm()
    return render(request, 'new-profile.html', {"form":form})

def profile(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    posts=Image.objects.filter(profile_id=current_user.id)
    return render(request, 'profile-page.html',{"profile":profile,"posts":posts})
    
@login_required(login_url='/accounts/login/')
def view_users(request, user_id):
    profile_pic= Profile.objects.filter(id=user_id).all()
    my_photos = Image.objects.filter(profile_id=user_id)
    users=User.objects.filter(id=user_id).all()

    return render(request, "other.html", {"photos":my_photos, "profile":profile_pic, "users":users})

def login_page(request):
    return render(request, 'come.html')
