from django.urls import path
from .views import *

urlpatterns = [
    path("",index , name="index"),
    path("signup", signup , name="signup"),
    path("signin", signin , name="signin"),
    path("logout", logout , name="logout"),
    path("settings", settings , name="settings"),
    path("upload", upload , name="upload"),
    path("like_post", like_post , name="like_post"),
    path("follow", follow , name="follow"),
    path('profile/<str:pk>', profile, name='profile'),
    path('search', search, name='search'),

]