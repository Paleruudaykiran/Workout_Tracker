from django.contrib import admin
from .models import Room , Topic,Message,Challenges,Workout,Workout_categories,Goals

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Challenges)
admin.site.register(Workout_categories)
admin.site.register(Workout) 
admin.site.register(Goals)
