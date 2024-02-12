"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
# from chat_room import views
# from myapp.views import prec
app_name = 'myapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('mandi/', views.price,name='price'),
    path('about/', views.about,name='about'),
    path('blog/', views.blog,name='blog'),
    path('contact/', views.contact,name='contact'),
    path('tools/', views.tools,name='tools'),

    # chat room
    path('Chat_home/', views.Chat_home,name=""),
    # path('<str:room>/',views.room,name="room"),
    path('checkview',views.checkview,name="checkview"),
    path('send',views.send,name="send"),
    path('getMessages/<str:room>/',views.getMessages,name="getMessages"),
    path('precesion/',views.precesion,name='precesion'),
    path('animals/',views.animals,name='animals'),
    
    # Authentication
    
    path('register',views.register, name="register"),
    path('login/',views.login, name="login"),
    path('user-logout',views.user_logout, name="user-logout"),
    #News
    path('subscriber/',views.subscriber,name='subscriber'),

]
