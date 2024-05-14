from django.db import models
from datetime import datetime

# Create your models here.
class SendMessage(models.Model):
    sender_user_email = models.EmailField(max_length=100, unique=False)
    date_sent = models.DateTimeField(blank= False , default= datetime.strptime(datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),"%d/%m/%Y, %H:%M:%S"))
    message_content = models.CharField(blank= False , max_length=10000)
    receiver_user_email = models.EmailField(max_length=100, unique=False)

    def __str__(self):
        return f"sender: {self.sender_user_email} ,date: {self.date_sent} , message: {self.message_content} , receiver: {self.receiver_user_email}"
