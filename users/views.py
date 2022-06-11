from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm , UserUpdateForm, ProfileUpdateForm
from .models import Profile 
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.apps import apps 


Room = apps.get_model('myapp','Room')
Challenges = apps.get_model('myapp','Challenges')
Goals = apps.get_model('myapp','Goals')
Message = apps.get_model('myapp','Message')
# Plans = apps.get_model('myapp','Plans') 
# Workout_plans = apps.get_model('myapp','Workout_Plans') 

def register(request) :
    if request.method == 'POST' :
        form = UserRegisterForm(request.POST) 
        if form.is_valid() :
            form.save()
            username = form.cleaned_data.get('username') 
            u = User.objects.get(username=username)
            obj = Profile(
                user = u,
                image = 'profile_pics/default.jpg',
            )
            obj.save() 
            return redirect('login')
    else :
        form = UserRegisterForm() 
    return render(request,'register.html',{'form':form})

@login_required
def profile(request) :
    challenges = Challenges.objects.filter(user = request.user)
    goals = Goals.objects.filter(participant = request.user) 
    message = Message.objects.filter(user = request.user) 
    rooms = Room.objects.filter(host=request.user) 

    if request.method == 'POST' :
        u_form = UserUpdateForm(request.POST,
        request.FILES,
        instance=request.user) 
        p_form = ProfileUpdateForm(request.POST,
        instance=request.user.profile) 
        if u_form.is_valid() and p_form.is_valid() :
            u_form.save() 
            p_form.save() 
            return redirect('profile')
    else :
        u_form = UserUpdateForm(instance=request.user) 
        p_form = ProfileUpdateForm(instance=request.user.profile) 

    context = {
               'u_form' : u_form , 
               'p_form' : p_form, 
               'challenges_count' : len(list(challenges)),
               'goals_count' : len(list(goals)),
               'messages' : message,
               'rooms_count' : len(list(rooms)),
               'rooms' : rooms,
               'challenges' : challenges
              }

    return render(request,'profile.html',context)

