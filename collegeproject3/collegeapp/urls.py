from.import views
from django.urls import path




urlpatterns = [

    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('form', views.form, name='form'),
    path('newpage', views.newpage, name='newpage'),
    path('get_branches', views.get_branches, name="get-branch"),
    path('message',views.message,name='message'),

]