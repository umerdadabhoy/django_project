from django.urls import path , re_path

from . import views

urlpatterns=[
    path('', views.user_register, name="users.register"),
    path('login/', views.user_login, name="users.login"),
    
    #non-views
    re_path(r"^logout", views.user_logout, name="users.logout" ),
    
    re_path(r'^check_email', views.check_email, name="users.check_email"),
]