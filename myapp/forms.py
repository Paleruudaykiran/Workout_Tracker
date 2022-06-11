from .models import Room
from django.forms import ModelForm
from .models import Message,Challenges

class RoomForm(ModelForm) :
    class Meta : 
        model = Room 
        fields = ['topic','name','description']


class MessageForm(ModelForm) :
    class Meta : 
        model = Message 
        fields = ['body']

class ChallengesForm(ModelForm) :
    class Meta : 
        model = Challenges 
        fields = ['title','description','image']