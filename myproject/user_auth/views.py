from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from base.models import CartModels
User=get_user_model()


# Create your views here.

def login_(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
       

        if user is not None:
            login(request, user)

            # Role-based redirect
            if user.role == 'vendor':
                return redirect('vendor_dashboard')
            else:
                return redirect('home')

        else:
            return render(request, 'login_.html', {'status': 'Invalid credentials','search_bar': True})

    return render(request, 'login_.html')

def register(request):
    
    if request.method == 'POST':
        # Handle registration logic here
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        
        try:
            existing_user = User.objects.get(username=username)
            return render(request, 'register.html', {'status': 'Username already exists'})
        except:
            s=User.objects.create(username=username, email=email, password=password, role=role)
            s.set_password(password)
            s.save()
            return redirect('login_')

    return render(request, 'register.html', {'search_bar': True})

@login_required(login_url='login_')
def profile(request):
    cartProducts_count=CartModels.objects.filter(host=request.user).count()

    return render(request, 'profile.html', {'search_bar': True, 'cartProducts_count': cartProducts_count})

@login_required(login_url='login_')
def logout_(request):
    logout(request) 
    return redirect('login_')

def forget_pass(request):
    if request.method=='POST':
        a=request.POST.get('username')
        try:
            u=User.objects.get(username=a)
            request.session['fp_user']=u.username
            return redirect('reset_pass')
        except:
            return render(request,'forget_pass.html',{'error':True, 'search_bar': True})
    return render(request,'forget_pass.html',{'search_bar': True})

def reset_pass(request):
    
    u=request.session.get('fp_user')
    if u is None:
        return redirect('forget_pass')
    user=User.objects.get(username=u)
    if request.method == 'POST':
        new=request.POST['confirm_password']
        if user.check_password(new):#true if passward which user entered is same as the old password
            
            return render(request,'reset_pass.html',{'same':True})
        user.set_password(new)
        user.save()
        del request.session['fp_user'] #deletes the username stored in session storage
        return redirect('login_')
        
        
    return render(request,'reset_pass.html',{'search_bar': True})
    
def new_pass(request):
    if request.method == 'POST':
        if 'oldpasw' in request.POST:
            a = request.POST['oldpasw']
            auth = authenticate(username=request.user.username,password=a)
            
            if auth:
                return render(request,'new_pass.html',{'new_pass':True})
            else:
                return render(request,'new_pass.html',{'wrong':True})
        if 'newpasw' in request.POST:
            b=request.POST['newpasw']
            if request.user.check_password(b): #check if the new password entered by the user is same as old password
                return render(request,'new_pass.html',{'same':True})
            request.user.set_password(b)
            request.user.save()
            return redirect('login_')
    return render(request,'new_pass.html',{'search_bar': True})

    
