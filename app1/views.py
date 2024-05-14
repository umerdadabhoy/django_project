from django.shortcuts import render , redirect
from django.http import HttpResponse ,HttpResponseRedirect

from users.views import check_login

from .models import SendMessage
from .forms import SendMessageForm
# Create your views here.
#@check_login
@check_login
def index(request):
    
    data = {}

    form = SendMessageForm(request.POST or None,initial={'sender_user_email': request.user})

    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('app1.index')
            

    return render(request , 'app1/index.html' , data)

@check_login
def messages_sent_to_self(request):
    messages = SendMessage.objects.filter(sender_user_email = request.user, receiver_user_email = request.user).values_list("date_sent","message_content")
    messages = list(messages)
    context = {'messages': messages, 'sender':'Self', 'receiver':'Self'}
    
    
    return render(request,"app1/messages_sent_to_self.html" , context)


def messages_sent_to_others(request):
    
    messages = SendMessage.objects.filter(sender_user_email = request.user).exclude(receiver_user_email = request.user).values_list("date_sent","receiver_user_email","message_content")
    messages = list(messages)
    context = {'messages': messages, 'sender':'Self', 'receiver':'Others'}
    
    
    return render(request,"app1/messages_sent_to_others.html" , context)

def messages_received(request):
    
    messages = SendMessage.objects.filter(receiver_user_email = request.user).exclude(sender_user_email = request.user).values_list("date_sent","sender_user_email","message_content")
    messages = list(messages)
    context = {'messages': messages, 'sender':'Others', 'receiver':'You'}
    
    
    return render(request,"app1/messages_received.html" , context)


