from django.shortcuts import render,redirect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User

from App_BLog.forms import UserRegistrationForm, UserEditForm, AvatarForm, ArticleForm
from App_BLog.models import Article, Avatar
from datetime import datetime



from django.views.generic.detail import DetailView
# Create your views here.

def index(request):
  
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user.id)
        if len(avatar)>0:
            if len(avatar) == 1:
                return render(request, 'index.html', {"url": avatar[0].image.url})
            else:
                return render(request, 'index.html', {"url": avatar[len(avatar)-1].image.url})
            
        else: 
            
            return render(request, 'index.html')
    else: 
            
        return render(request, 'index.html')



def login_req(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data= request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(username = username, password = password)
            
            if user is not None:
                login(request, user)
                
                return render(request, "index.html", {"user":user})
            else:
                return render(request, "login.html", {"form":form,"mensaje": "Usuario o contraseña incorrecta"})
        
        else :
            return render(request, "login.html", {"form":form,"mensaje":"Datos incorrectos"})
        
    form = AuthenticationForm()
    return render(request, "login.html", {"form":form})




def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
           username =  form.cleaned_data.get("username")
           password =  form.cleaned_data.get("password")
    
           user =  form.save()
           login(request,user)
           return render(request, "index.html", {"username":username})

        else:
            return render(request, "register.html", {"form":form, "mensaje":"Error en datos"})
    
    
    form = UserRegistrationForm()
        
    return render(request, "register.html", {"form":form})


def getArticles(request):
     articles = Article.objects.all()
     print(articles)
     
     if request.method =="DELETE":
         pass
     else:
        return render(request,"articles.html", {"articles":articles})

@login_required
def articleForm(request):
     
     if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False) 
          
            article.author = request.user
            article.save()
            
            return render(request,"index.html")
     
     form = ArticleForm()      
     return render(request,"add-article.html", {"form":form}) 
 
def aboutMe(request):
    return render(request, "aboutMe.html")


def avatar(request):

    if request.method == "POST":
        print("Post")
        formulario = AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():

            user = User.objects.get(username=request.user)   
            avatar = Avatar(user=user, image=formulario.cleaned_data.get("image"))
            avatar.save()

            return render(request, 'index.html')

    formulario = AvatarForm()

    return render(request, 'avatar.html', {"formulario": formulario})

 
class ArticleDetails(DetailView):

    model = Article
    template_name = 'article-details.html'