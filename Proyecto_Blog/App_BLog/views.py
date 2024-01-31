from django.shortcuts import render,redirect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
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
                return render(request, "login.html", {"mensaje": "Usuario o contraseña incorrecta"})
        
        else :
            return render(request, "login.html", {"mensaje":"Datos incorrectos"})
        
    
    return render(request, "login.html")




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
        article_to_delete = Article.objects.get(id=article_id)
        article_to_delete.delete()
    articles = Article.objects.all().order_by('-create_at')
    my_articles = []
    
     
    
    for article in articles:
        if article.author == request.user:
            my_articles.append(article)
   
     
    
    avatar = Avatar.objects.filter(user=request.user.id)
    if len(avatar)>0:
        if len(avatar) == 1:
            return render(request,'articles.html',{"articles":my_articles, "url": avatar[0].image.url})
        else:
            return render(request, 'articles.html', {"articles":my_articles,"url": avatar[len(avatar)-1].image.url})
    
    else:
         return render(request, 'articles.html', {"articles":my_articles,"url": None})
    

@login_required
def articleForm(request):
    form = ArticleForm()   
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
           
            article = Article(title=form.cleaned_data.get("title"), subtitle = form.cleaned_data.get("subtitle"), description = form.cleaned_data.get("description"), author = request.user,image = form.cleaned_data.get("image") )
            article.save()
         
           
            
            return redirect("/app")
     
    
    avatar = Avatar.objects.filter(user=request.user.id)
    if len(avatar)>0:
        if len(avatar) == 1:
            return render(request,"add-article.html",{"form":form, "url": avatar[0].image.url})
        else:
            return render(request, "add-article.html", {"form":form,"url": avatar[len(avatar)-1].image.url})     
    else:
        return render(request, "add-article.html", {"form":form,})
 
def aboutMe(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    if len(avatar)>0:
        if len(avatar) == 1:
            return render(request,"aboutMe.html" ,{"url": avatar[0].image.url})
        else:
            return render(request, "aboutMe.html" , {"url": avatar[len(avatar)-1].image.url})  
    else:
        return render(request, "aboutMe.html" , {"url": None}) 


def avatar(request):

    if request.method == "POST":
        print("Post")
        formulario = AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():

            user = User.objects.get(username=request.user)   
            avatar = Avatar(user=user, image=formulario.cleaned_data.get("image"))
            avatar.save()

            return redirect('profile') 

    formulario = AvatarForm()

    return render(request, 'avatar.html', {"formulario": formulario})

@login_required
def profile(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user.id)
    
    if len(avatar)>0:
        if len(avatar) == 1:
            return render(request,'profile.html',{ "user":user,"url": avatar[0].image.url})
        else:
            return render(request,'profile.html',{ "user":user,"url": avatar[len(avatar)-1].image.url}) 
       
    
    return render(request,'profile.html',{ "user":user})
   
  
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
            avatar = Avatar.objects.filter(user=request.user.id)
            if len(avatar)>0:
                if len(avatar) == 1:
                    return render(request, "profile.html", {"user":usuario, "url": avatar[0].image.url})
                else:
                    return render(request, "profile.html", {"user":usuario, "url": avatar[len(avatar)-1].image.url})
            else:
                 return render(request, "profile.html", {"user":usuario})      
        
    form=UserEditForm(initial={"username":usuario.username, "first_name": usuario.first_name, "last_name": usuario.last_name,"email":usuario.email})
    
    avatar = Avatar.objects.filter(user=request.user.id)
    if len(avatar)>0:
        if len(avatar) == 1:
            return render(request,'update_profile.html',{ "form":form,"url": avatar[0].image.url})
        else:
            return render(request,'update_profile.html',{ "form":form,"url": avatar[len(avatar)-1].image.url}) 
    else:
        return render(request, "update_profile.html" , {"form":form,"url": None}) 
    
            
            
def update_article(request, dato):
        
    article = Article.objects.get(id= dato)

    if request.method =="POST":
                
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            article.title = info.get('title')
            article.subtitle = info.get('subtitle')
            article.description = info.get('description')
            article.image = info.get('image')
          
          
            article.save()
            
            return redirect("/app/articles")

    
    form = ArticleForm(initial= {"title":article.title,"subtitle":article.subtitle,"description":article.description,"image":article.image,"author": request.user})
    avatar = Avatar.objects.filter(user=request.user.id)
    if len(avatar)>0:
        if len(avatar) == 1:
            return render(request,'update_article.html',{ "form":form,"dato":dato,"url": avatar[0].image.url})
        else:
            return render(request,'update_article.html',{ "form":form,"dato":dato,"url": avatar[len(avatar)-1].image.url}) 
    else:
        return render(request, "update_article.html" , {"form":form,"dato":dato,"url": None}) 
 


def search(request):
    if request.method == "GET":
        search = request.GET.get("search")
        select = request.GET.get("select")
        if search:
            avatar = Avatar.objects.filter(user=request.user.id)
         
            if select == "title":
               title = Article.objects.filter(title__icontains = search) 
               return render(request,"search.html",{"result":title,"select":select})
            else:
                articles = Article.objects.all()
                author= []
                search =search.lower()
                for article in articles:
                    if article.author.first_name.lower() == search or article.author.last_name.lower() == search or article.author.username.lower() == search:
                        author.append(article)
                if len(avatar)>0:
                    if len(avatar) == 1: 
                        return render(request,"search.html",{"result":author,"select":select,"url": avatar[0].image.url })
                    else:
                        return render(request,"search.html",{"result":author,"select":select,"url":avatar[len(avatar)-1].image.url })
        else:
            avatar = Avatar.objects.filter(user=request.user.id)
            if len(avatar)>0:
                if len(avatar) == 1: 
                    return render(request,"search.html",{"result":None,"select":select,"url": avatar[0].image.url})
                else:
                    return render(request,"search.html",{"result":None,"select":select,"url": avatar[len(avatar)-1].image.url})
                     
    
           
    return render(request,"index.html") 
     
 
class ArticleDetails(DetailView):
       
    model = Article
    template_name = 'article-details.html'
    
    
   
 