from django.shortcuts import render, HttpResponse, redirect
from Blog_Post.models import Blog
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import CreateView
import datetime
from .models import Contact
# Create your views here.
def index(request):
    
    posts = Blog.objects.order_by('-date')[:10]
    blogs = Blog.objects.filter(username='Ishan')
    blogs = blogs.order_by('-date')[:10]
    return render(request,'index.html',{'posts':posts,'blogs':blogs})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        subject = request.POST['subject']
        content = request.POST['content']

        if fname != ' ' and lname != ' ' and email != ' ' and subject != ' ' and content != ' ':
            messages.success(request,'Successfully Submitted Your request')
            data = Contact.objects.create(fname=fname,lname=lname,email=email,subject=subject,date=datetime.datetime.now(),desc=content)
            data.save()
            return redirect('/')
        else:
            messages.error(request,'Please Fill out the form carefully')
            return redirect('contact')
    return render(request,'contact.html')
def search(request):
    query = request.GET['query']
    postsTitle = Blog.objects.filter(title__icontains=query)
    postsContent = Blog.objects.filter(content__icontains=query)
    posts = postsTitle.union(postsContent)
    return render(request,'search.html',{'posts':posts,'query':query})

def create(request):
    if request.method == 'POST':
        Profile = request.user.profile.image.url
        title = request.POST['title']
        content = request.POST['content']
        designation = request.user.profile.designation
        date = datetime.datetime.now()
        category = request.POST['category']
        
        if content != '' and title != '':
            Blog.objects.create(profile=Profile,title=title,username=request.user,designation=designation,date=date,category=category,content=content)
            messages.success(request,'Blog Posted Successfully')
        else:
            messages.error(request,'Please Fill out all the fields')
    return render(request,'create_blog.html')

def manageAccounts(request):
    return render(request,'manageAccounts/manageAccountsHome.html')

class AddPostView(CreateView):
    model = Blog
    template_name = 'create_blog.html'
    fields = '__all__'

    