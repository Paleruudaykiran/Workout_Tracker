from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Topic,Room,Message,Challenges,Workout,Workout_categories,Goals
from django.db.models import Q
from .forms import RoomForm, MessageForm, ChallengesForm
from django.contrib.auth.decorators import login_required


def home(request) :
    categories = Workout_categories.objects.all() 
    context = {'categories' : categories}
    return render(request,'home.html',context=context)

def forum(request) :
    q = request.GET.get('q')  if request.GET.get('q') != None else ''
    
    rooms = Room.objects.filter(
                                 Q(topic__name__icontains=q) | 
                                 Q(name__icontains=q) |
                                 Q(description__icontains=q))
    topics = Topic.objects.all() 
    context = {'topics' : topics, 'rooms' : rooms, 'topics_count' : topics.count(),'rooms_count' : rooms.count()} 
    return render(request,'forum.html',context=context) 


def room(request,pk) :
    room = Room.objects.get(id = pk) 
    room_messages = room.message_set.all() 
    topics = Topic.objects.all() 
    msg_count = room_messages.count()
    if request.method == 'POST' : 
        print(request.POST)
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST['body']
        )
        message.save()
    context = {'room' : room,'messages':room_messages,'topics' : topics,'msg_count':msg_count} 
    return render(request,'room.html',context=context)

@login_required
def create_room(request) :
    form = RoomForm() 
    if request.method == 'POST' :
        form = RoomForm(request.POST)
        if form.is_valid() : 
            room = form.save(commit=False) 
            room.host = request.user
            form.save() 
    context = {'form' : form}
    return render(request,'create_room.html',context)

@login_required
def delete_room(request,pk) :
    room = Room.objects.get(id=pk) 
    if request.user != room.host : 
        return HttpResponse('You are not allowed hear')
    if request.method == 'POST' : 
        room.delete() 
        return redirect('home')
    return render(request,'delete.html',{'obj':room})

@login_required()
def delete_message(request,pk) : 
    message = Message.objects.get(id=pk) 
    if request.user != message.user : 
        return HttpResponse('You are not allowed hear')
    if request.method == 'POST' : 
        message.delete() 
        return redirect('forum')
    return render(request,'delete.html',{'obj':message})


def update_room(request,pk):
    room = Room.objects.get(id=pk) 
    form = RoomForm(instance=room) 

    if request.method == 'POST' :
        form = RoomForm(request.POST,instance=room) 
        if form.is_valid() : 
            form.save() 
            return redirect('home')
    context = {'form':form} 
    return render(request,'create_room.html',context)


def update_msg(request,pk) :
    print('called')
    msg = Message.objects.get(id=pk) 
    form = MessageForm(instance=msg) 

    if request.method == 'POST' :
        form = MessageForm(request.POST,instance=msg) 
        if form.is_valid() :
            form.save() 
            return redirect('forum') 
    context = {'form' : form } 
    return render(request,'create_msg.html',context) 

@login_required
def challenges(request) :
    challenges = Challenges.objects.all() 
    goals = Goals.objects.filter(participant=request.user) 
    lis = []
    for x in goals :
        y = x.__str__()
        lis.append(y)
    context = {'challenges':challenges,'lis':lis}
    return render(request,'challenges.html',context=context) 

@login_required
def goals(request) :
    goals = Goals.objects.filter(participant=request.user) 
    print(goals) 
    context = {'goals' : goals}
    return render(request,'goals.html',context=context)

@login_required()
def delete_goal(request,pk) : 
    goal = Goals.objects.get(id=pk) 
    if request.user != goal.participant : 
        return HttpResponse('You are not allowed hear')
    if request.method == 'POST' : 
        goal.delete() 
        return redirect('goals')
    return render(request,'delete.html',{'obj':goal})

@login_required 
def participate_challenge(request,pk) :
    challenge = Challenges.objects.get(id=pk)
    goal = Goals(
        goal = challenge,
        completed = False,
        participant = request.user,
    )
    goal.save() 
    return redirect('goals')

def challenge_completed(request,pk) :
    goal = Goals.objects.get(id=pk) 
    goal.completed = True 
    goal.save() 
    return redirect('goals') 

def create_challenge(request) :
    form = ChallengesForm() 
    if request.method == 'POST' :
        form = ChallengesForm(request.POST)
        if form.is_valid() : 
            challenge = form.save(commit=False) 
            challenge.user = request.user
            form.save() 
        return redirect('challenges')
    context = {'form' : form}
    return render(request,'create_challenge.html',context)

def challenge_delete(request,pk) :
    challenge = Challenges.objects.get(id=pk) 
    challenge.delete() 
    return redirect('challenges')

def challenge_update(request,pk) :
    challenge = Challenges.objects.get(id=pk) 
    form = ChallengesForm(instance=challenge) 

    if request.method == 'POST' :
        form = ChallengesForm(request.POST,instance=challenge) 
        if form.is_valid() :
            form.save() 
            return redirect('challenges') 
    context = {'form' : form } 
    return render(request,'create_challenge.html',context) 

def workouts(request,pk) : 
    workouts = Workout.objects.filter(category_id=pk) 
    categories = Workout_categories.objects.all()
    context = {'workouts' : workouts, 'categories' : categories} 
    print(workouts)
    return render(request,'workouts.html',context=context)