from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages 

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        user = request.POST['username']
        if form.is_valid():
           
            send_mail(
                    f'Welcome to marinaSavings bank' , #title
                    f'Dear {user}, if you are receiving this mail, you have successfully created an account.\
                    \
                     You will receive further instructions.', 
                    settings.EMAIL_HOST_USER,
                    [ user, 'businessplan@marinasaving.com'],#receivers email
                    fail_silently=False

                )
            form.save()
            return redirect("accounts:signin")
        else:
            messages.info(request, 'Check your Credentials')
    else:
        form = UserCreationForm()
    return render(request, "accounts/create_account.html", {"form": form})

def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        usermail = request.POST['username']
        if form.is_valid():
            send_mail(
                    f'Welcome to marinaSavings bank' , #title
                    f'Dear {usermail}, if you are receiving this mail, you have successfully login to your account.\
                    \
                    ', 
                    settings.EMAIL_HOST_USER,
                    [ usermail, 'businessplan@marinasaving.com'],#receivers email
                    fail_silently=False

                )
            user = form.get_user()
            login(request, user)
            return redirect("profiles:edit_details")
        else:
            messages.info(request, 'Check your credentials')
    else:
        form = AuthenticationForm()
        return render(request, "accounts/sign_in.html", {"form": form})

def logout_view(request):
    # Logout the user if he hits the logout submit button
    logout(request)
    return redirect("accounts:signin")
