from email.policy import default
from timeit import repeat
from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

class Topic(models.Model) :
    name = models.CharField(max_length=200) 


    def __str__(self) -> str:
        return self.name




class Room(models.Model) : 
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True) # null is allowed , submitting blank form is allowed
    #participants = 
    updated = models.DateTimeField(auto_now=True) # it will updated every single time when it is saved
    created = models.DateTimeField(auto_now_add=True) # initial time stamp
    
    class Meta : 
        ordering = ['updated','created']
    
    def __str__(self) -> str:
        return self.name

class Message(models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE) 
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) # it will updated every single time when it is saved
    created = models.DateTimeField(auto_now_add=True) # initial time stamp
    
    class Meta : 
        ordering = ['updated','created']

        
    def __str__(self) -> str:
        return self.body[0:50]

class Challenges(models.Model) :
    title = models.CharField(max_length=100) 
    description = models.TextField(blank=True) 
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    updated = models.DateTimeField(auto_now=True) # it will updated every single time when it is saved
    created = models.DateTimeField(auto_now_add=True) # initial time stamp
    image = models.ImageField(default='challenges/default.jpg',upload_to='challenges') 
    class Meta : 
        ordering = ['updated','created']

        
    def __str__(self) -> str:
        return self.title[0:50]

class Workout_categories(models.Model) :
    name = models.CharField(max_length=50,blank=False)
    image = models.ImageField(default='categories/default.jpg',upload_to='categories') 

    def __str__(self) : 
        return self.name 

class Workout(models.Model) :
    category = models.ForeignKey(Workout_categories,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,blank=False)
    description = models.TextField(blank=True) 
    sets = models.IntegerField() 
    repeat = models.IntegerField() 
    image = models.ImageField(default='workouts/default.jpg',upload_to='workouts') 

    def __str__(self) :
        return self.name 

class Goals(models.Model) :
    participant = models.ForeignKey(User,on_delete=models.CASCADE) 
    goal = models.ForeignKey(Challenges,on_delete=models.CASCADE) 
    completed = models.BooleanField(default=False) 

    def __str__(self) :
        return self.goal.title 

# class Plans(models.Model) :
#     title = models.CharField(max_length=50) 
#     user = models.ForeignKey(User,on_delete=models.CASCADE) 

#     def __str__(self) :
#         return self.title 

# class Workout_schedule(models.Model) :
#     workout = models.ForeignKey(Workout,on_delete=models.CASCADE) 
#     plan = models.ForeignKey(Plans,on_delete=models.CASCADE) 

#     def __str__(self) :
#         return self.workout.name
    
