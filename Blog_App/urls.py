from django.urls import path, include
from . import views
from .views import AddPostView
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('search',views.search,name='search'),
    path('create',views.create,name='create'),
    path('manageAccounts',views.manageAccounts,name='manageAccounts')
]
