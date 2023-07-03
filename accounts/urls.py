from django.urls import path, include
from . import views

urlpatterns = [
    path('signUp',views.signUp,name='signUp'),
    path('login',views.login,name='login'),
    path('logout',views.log_out,name='log_out'),
    path('update',views.update,name='updateProfile'),
    path('manageBlog',views.manageBlog,name='manageBlog'),
    path('forgotPassword',views.forgotPassword,name='forgotPassword'),
    path('resetPassword',views.resetPassword,name='resetPassword')
]