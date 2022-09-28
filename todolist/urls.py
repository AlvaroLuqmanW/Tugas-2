from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', login_user, name='login'),
    path('create-task/', show_createtask, name='show_createtask'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout')
]