from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'layout.html')

@login_required
def redirect_to_edit_profile(request):
    username = request.user.profile.username
    return redirect('edit_profile', username=username)