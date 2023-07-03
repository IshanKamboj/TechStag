from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib import messages
from Blog_Post.models import Blog
from django.core.mail import send_mail
from Blog.settings import EMAIL_HOST_USER
# Create your views here.
def signUp(request):
    try:
        if request.method == 'POST':
            fname = request.POST['full_name']
            temp = False
            if ' ' in fname:
                fname,lname = fname.split(' ')
                temp = True
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            username = request.POST['username']
        
            if User.objects.filter(username = request.POST['username']).exists():
                messages.error(request,'Username Taken')
            elif User.objects.filter(email = request.POST['email']).exists():
                messages.error(request,'Email already exists')
            else:
                
                if password1 == password2:
                    if len(password1) >= 8:
                        if temp:
                            user = User.objects.create_user(username=username,first_name=fname,last_name=lname,password=password1,email=email)
                            messages.success(request,'Account created successfully')
                            return redirect('/')
                        else:
                            user = User.objects.create_user(username=username,first_name=fname,password=password1,email=email)
                            messages.success(request,'Account created successfully')
                            return redirect('/')
                    else:
                        messages.error(request,'Password Length did not match')
            
            
                else:
                    messages.error(request,'Error in Submitting. Please Check that all field are filled correctly')
                    return render(request,'accounts/signup.html')
    except ValueError:
        messages.error(request,'Please Fill out all the fields')
        return render(request,'accounts/signup.html')
    return render(request,'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        elif not User.objects.filter(username = request.POST['username']).exists():
            messages.error(request, 'User Does Not Exists. Try creating an account')
            return redirect('/')
        else:
            
            messages.error(request,'Invalid Credentials. Try again')
            return redirect('/')
def log_out(request):
    logout(request)
    messages.success(request,'Logged Out successfully')
    return redirect('/')

def update(request):
    if request.method == 'POST':
        fname  = request.POST['fname']
        lname  = request.POST['lname']
        #print(lname)
        email  = request.POST['email']
        designation  = request.POST['designation']
        
        if fname == request.user.first_name and lname == request.user.last_name and email == request.user.email and designation == request.user.profile.designation:
            messages.warning(request,'No Change Detected')
        else:
            if fname != request.user.first_name or lname != request.user.last_name or email != request.user.email or designation != request.user.profile.designation:
                d = Profile.objects.get(user=request.user)
                d.designation = designation
                
                u = User.objects.get(username=request.user)
                u.first_name = fname
                u.last_name = lname
                u.email = email
                d.save()
                u.save()
                messages.success(request,'Successfully updated Your Details')
                return redirect('updateProfile')
    print()
    return render(request,'manageAccounts/update.html')

def manageBlog(request):
    blogs = Blog.objects.filter(username=request.user)
    return render(request,'manageAccounts/manageBlog.html',{'blogs':blogs})
def forgotPassword(request):
    if request.method == 'POST':
        if User.objects.filter(email = request.POST['email']).exists():
            email = request.POST['email']
            send_mail(
                        'Password Reset',
                        'This a mail regarding Password Reset of Blog Website Account.',
                        EMAIL_HOST_USER,
                        [email],
                        fail_silently=False,
                    )
            messages.success(request,'An email has been sent to your account check your email for more details')
        else:
            messages.error(request,'Email not registered.')
    return redirect('/')

def resetPassword(request):
    if request.method == 'POST':
        oldPass = request.POST['oldPass']
        newPass1 = request.POST['newPass1']
        newPass2 = request.POST['newPass2']
        if request.user.check_password(raw_password=oldPass):
            if newPass1 == newPass2:
                if len(newPass1) >= 8:
                    messages.success(request,'Password updated successfully')
                    u = User.objects.get(username=request.user)
                    u.set_password(newPass1)
                    u.save()
                    logout(request)
                    messages.success(request,'Password changed successfully. Please Login again.')
                    return redirect('/')
                else:
                    messages.error(request,'New password must be 8 or more characters long.')
                    return redirect('manageAccounts/resetPassword.html')
                #return render(request,'manageAccounts/resetPassword.html')
            else:
                messages.error(request,'Re-typed Password did not match')
                return render(request,'manageAccounts/resetPassword.html')
        else:
            messages.error(request,'Old Password entered did not match')
            return render(request,'manageAccounts/resetPassword.html')
        
