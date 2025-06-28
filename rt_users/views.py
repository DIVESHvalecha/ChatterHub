from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.models import User
from .forms import ProfileForm
from .models import profile
from django.contrib.auth.decorators import login_required


# Create your views here.

def profile_view(request, username):
    print(f"Profile view requested for username: {username}")
    profilee = get_object_or_404(profile, username=username)
    return render(request, 'profile.html', {'profile': profilee})

@login_required
def edit_profile(request, username):
    profilee = get_object_or_404(profile, username=username)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profilee)
        if form.is_valid():
            form.save()
            return redirect('Profile_view', username=request.user.profile.username)
    else:
        form = ProfileForm(instance=profilee)  
    return render(request, 'edit_profile.html', {'form': form})