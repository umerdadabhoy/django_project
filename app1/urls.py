from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name="app1.index"),
    path('messages_sent_to_self', views.messages_sent_to_self, name="app1.messages_sent_to_self"),
    path('messages_sent_to_others',views.messages_sent_to_others  , name="app1.messages_sent_to_others"),
    path('messages_recieved' , views.messages_received , name="app1.messages_received"),
]