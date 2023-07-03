from django.urls import path, include
from . import views

urlpatterns = [
    path('latestBlog',views.latest,name='latest'),
    path('popularBlog',views.popular,name='popular'),
    path('allBlog',views.allBlog,name='allBlog'),
    path('<int:pk>',views.fullBlog,name='fullBlog'),
    
]

