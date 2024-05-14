from django import forms
from .models import SendMessage
from users.models import User


#form for sending message
class SendMessageForm(forms.ModelForm):
    

    class Meta:
        model = SendMessage
        fields = "__all__"
        exclude = ['date_sent']
        widgets = {
            'sender_user_email':forms.HiddenInput(),
            'message_content' : forms.Textarea(attrs={'default': '','cols': 80, 'rows': 5 , 'placeholder':'Write your message here','required':True,'style': "width:100%;"} ),
            #this query allows the option to only send email to non superusers accounts that are active
            'receiver_user_email' : forms.Select(attrs={'default': ''} , choices=list(User.objects.filter(is_superuser = 0, is_active = 1).values_list('email','email')))
        }