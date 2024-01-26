from django.contrib import admin
from django.urls import path 
from .views import index, login_req, register,articleForm, getArticles, aboutMe, avatar,profile, update_profile,update_article,search,ArticleDetails
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("",index, name="inicio"),
    path("login/",login_req,name="login"),
    path("register/",register,name="register"),
    path("new-article/",articleForm,name="add_article"),
    path("articles/", getArticles,name="articles" ),
    path('article-detail/<pk>', ArticleDetails.as_view(), name='article-detail'),
    path("aboutMe/", aboutMe, name="about"),
    path('avatar/', avatar, name='avatar'),
    path("profile/", profile, name="profile"),
    path("update/", update_profile, name="update_profile"),
    path("update-article/<dato>", update_article, name="update_article"),
    path("logout/",LogoutView.as_view(template_name="logout.html" ), name="logout" ), 
     path("search/",search,name="search"),
   
    ]