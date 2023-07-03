from django.shortcuts import render
from .models import Blog
# Create your views here.
def latest(request):
    posts = Blog.objects.order_by('-date')

    return render(request,'blogPosts/latestBlog.html',{'posts':posts})

def popular(request):
    blogs = Blog.objects.all()
    return render(request,'blogPosts/popularBlog.html',{'blogs':blogs})

def allBlog(request):
    posts =  Blog.objects.filter(username='Ishan')
    posts = posts.order_by('-date')
    return render(request, 'blogPosts/all_Blog.html', {'posts':posts})

def fullBlog(request, pk):
    posts = Blog.objects.filter(pk=pk)
    context={'posts':posts}
    return render(request, 'fullBlog.html',context)

