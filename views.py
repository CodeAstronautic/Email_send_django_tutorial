from django.shortcuts import render,redirect
from django.contrib.auth import logout, authenticate, login
from . form import SubscribeForm
from django.contrib import messages
from project.settings import EMAIL_HOST_USER
from . import form
from django.core.mail import send_mail
# Create your views here.
#DataFlair #Send Email
def subscribe(request):
    sub = form.SubscribeForm()
    if request.method == 'POST':
        sub = form.SubscribeForm(request.POST)
        subject = 'Welcome to DataFlair'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'templates/success.html', {'recepient': recepient})
    return render(request, 'templates/index.html', {'form':sub})

def index_page(request):
    return render(request,'templates/base.html')
'''
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect(index_page)
        
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request,"templates/register.html",{"form":form})

    form = UserCreationForm()
    return render(request,"templates/register.html",{"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect(index_page)
'''  