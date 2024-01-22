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
    
        all_articles = Article.objects.all().order_by('-create_at')
        if request.user.is_authenticated:
            avatar = Avatar.objects.filter(user=request.user.id)
            if len(avatar)>0:
                if len(avatar) == 1:
                    return render(request,'index.html',{"all_articles":all_articles, "url": avatar[0].image.url})
                else:
                    return render(request, 'index.html', {"all_articles":all_articles,"url": avatar[len(avatar)-1].image.url})
           
     
        return render(request, 'index.html', {"all_articles":all_articles})      
   
  
      
  



def login_req(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data= request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(username = username, password = password)
            
            if user is not None:
                login(request, user)
                
                return redirect( "/app", {"user":user})
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
           return redirect("/app", {"username":username})

        else:
            return render(request, "register.html", {"form":form, "mensaje":"Error en datos"})
    
    
    form = UserRegistrationForm()
        
    return render(request, "register.html", {"form":form})


def getArticles(request):
          
     if request.method =="POST":
         article_id = request.POST.get('article-id')
         print(article_id)
         article_to_delete = Article.objects.filter(id=article_id).first()
         article_to_delete.delete()
     articles = Article.objects.all()
     my_articles = []
     for article in articles:
         if article.author == request.user:
             my_articles.append(article)
     print(my_articles[0])
    
     return render(request,"articles.html", {"articles":my_articles})

@login_required
def articleForm(request):
     form = ArticleForm()   
     if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save() 
          
            article.author = request.user
            article.save()
           
            
            return redirect("/app")
     
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

            return redirect('/app/profile') 

    formulario = AvatarForm()

    return render(request, 'avatar.html', {"formulario": formulario})

@login_required
def profile(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user.id)
    if len(avatar)==0:
         return render(request,'profile.html',{ "user":user})
    
    return render(request,'profile.html',{ "user":user,"url": avatar[0].image.url}) 
   
  
    


def update_profile(request):
    usuario =request.user
    
    if request.method =="POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.username = info.get('username')
            usuario.first_name = info.get('first_name')
            usuario.last_name = info.get('last_name')
            usuario.email = info.get('email')
            usuario.password1 = info.get('password1')
            usuario.password2 = info.get('password2')
          
            usuario.save()
            
            return render(request, "profile.html", {"user":usuario})
            
            
    
    else:
        form = UserEditForm(initial= {"username":usuario.username,"email":usuario.email,"first_name":usuario.first_name, "last_name":usuario.last_name})
        
        return render(request,"update_profile.html", {"form":form, "usuario":usuario}) 
 
 
 
class ArticleDetails(DetailView):

    model = Article
    template_name = 'article-details.html'