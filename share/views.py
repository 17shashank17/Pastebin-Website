from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from share.forms import SignupForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from share.forms import Rich
from .models import RichText,User_Save
# Create your views here.

import random
import string


class Link:

    def get_random_link(self):
        b=string.ascii_letters
        q=random.choice(b)
        r=random.choice(b)
        s=random.randint(10,100)
        w=random.choice(b)
        t=random.choice(b)
        c=q+r+w+t+str(s)
        c=c+'/'
        return c



def home(request):
    if request.method=="POST":
        form=Rich(request.POST)

        if form.is_valid():
            post_item=form.save(commit=False)
            g=Link()
            d=g.get_random_link()
            post_item.content_link=d
            post_item.save()
            request.session['d']=d
            request.session['post']=post_item.id
            return HttpResponseRedirect(d)

    else:
        form = Rich()
    return render(request,'share/home.html',{"form":form})



def signup(request):

    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        conf_pass=request.POST.get("con_password")
        first=request.POST.get("first")
        last=request.POST.get("last")
        email=request.POST.get("email")
        if password != conf_pass or len(username)<8 or len(password)<8 or password=='' or first=='' or email=='':
            return render(request,'share/passwordnotmatch.html')
        try:
            user_check=User.objects.get(username=username)
            return render(request,'share/user_already_exist.html')
        except:
            user1=User()
            user1.username=username
            user1.set_password(str(password))
            user1.first_name=first
            user1.last_name=last
            user1.email=email
            user1.save()

            user=authenticate(username=username,password=password)
        

            login(request,user)

            return HttpResponseRedirect('/share')
    else:
        return render(request,"share/signup.html",{})

def profile(request):
    user=request.session['username']
    user_obj=User.objects.filter(username=user)
    user_to_show=User_Save.objects.filter(user_content=user_obj[0])
    args={'user_obj':user_obj, 'user_to_show':user_to_show}
    return render(request,'share/profile.html',args)

def login_user(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        request.session['username']=username
        user=authenticate(username=username,password=password)


        if user:
            login(request,user)
            #return render(request,'share/home.html')
            return HttpResponseRedirect('/share/home_afterlogin')
        else:
            return render(request,"share/invalid_user.html")
    else:
        return render(request,"share/login.html",{})

def home_afterlogin(request):
    user=request.session['username']
    if request.method=="POST":
        form=Rich(request.POST)
        
        if form.is_valid():
            post_item=form.save(commit=False)
            g=Link()
            d=g.get_random_link()
            post_item.content_link=d
            post_item.save()
            
            link='http://localhost:8000/share/'+str(d)
            
            
            user=request.session['username']
            user_obj=User.objects.filter(username=user)
            user_to_save=User_Save.objects.create(user_content=user_obj[0])
            user_to_save.user_content_link=link
            user_to_save.owner=user
            user_to_save.save()
            request.session['d']=d
            request.session['post']=post_item.id
            return HttpResponseRedirect(d)
    else:
        form = Rich()
    return render(request,'share/afterlogin.html',{"form":form, 'user':user})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/share')

def fetch_view(request):
    #c=request.session['d']
    #k=request.session['post']
    
    q=request.build_absolute_uri()
    q=q.split('/')
    form1=RichText.objects.get(content_link=q[4]+'/')
    print(form1.content_images)
    form=Rich(instance=form1)
    '''form=Rich()
    form.fields['content_images']=form1.content_images
    print(form1.content_images)
    print(form.fields['content_images'])
    form.save(commit=False)
    #form.fields['content_images']=form1.content_images
    #form['content_images']=(form1.content_images)
    #form=RichText.objects.get(content_link=q[4]+'/')'''
    return render(request,'share/fetch.html',{'form':form})