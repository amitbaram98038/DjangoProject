from django.shortcuts import redirect, render
from accounts.forms import SignUpForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm



# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,"Account created successfully")
            return redirect('home')
    else:
        form=SignUpForm()
    return render(request,'accounts/signup.html',{'form':form})

    def login_view(request):
        if request.method == 'POST':
            form=AuthenticationForm(data=request.POST)
            if form_is_valid():
                username= form.cleaned_data.get("username")
                password=form.cleaned_data.get('passowrd')
                user= authenticate(request,username=username, password= passowrd)
                if user is not None:
                    login(request, user)
                    next_url=request.POST.get('next') or request.GET('next')
                    return redirect(next_url or 'admin.index')
                else:
                    form= AuthenticationForm
                    return render(request, 'admin.index',{'form':form})