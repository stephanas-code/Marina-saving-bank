from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
from django.contrib import messages 
from django.core.mail import send_mail
from profiles.models import Status 
from django.contrib.auth.decorators import login_required
import random


def randomGen():
    # return a 6 digit random number
    return int(random.uniform(3105684900, 6105684900))

@login_required(login_url='accounts:signin')
def index(request):
    try:
        curr_user = Status.objects.get(user_name=request.user) # getting details of current user
    except:
        # if no details exist (new user), create new details
        curr_user = Status()
        curr_user.account_number = randomGen() # random account number for every new user
        curr_user.balance = 0
        curr_user.user_name = request.user
        curr_user.save()
    return render(request, "profiles/dashboard.html", {"curr_user": curr_user})

@login_required(login_url='accounts:signin')
def money_transfer(request):
    if request.method == "POST":
        form = forms.MoneyTransferForm(request.POST)
        pinform = forms.PinForm(request.POST)
        enter_your_account_id = request.POST['enter_your_account_id']
        pinuser = request.POST['pin']
        if form.is_valid():
            client = form.save(commit=False)
            
            if  models.pin.objects.filter(pin = pinuser ):
                client.sender = request.user            
            
                curr_user = models.MoneyTransfer()
                curr_user.sender = request.user
                curr_user.enter_your_account_id = request.POST['enter_your_account_id']
                curr_user.enter_the_destination_account_number =  request.POST['enter_the_destination_account_number']
                curr_user.enter_the_amount_to_be_transferred = request.POST['enter_the_amount_to_be_transferred']
                dest_user_acc_num = curr_user.enter_the_destination_account_number


                temp = curr_user # NOTE: Delete this instance once money transfer is done
                    
                dest_user = models.Status.objects.get(account_number=dest_user_acc_num) # FIELD 1
                transfer_amount = curr_user.enter_the_amount_to_be_transferred # FIELD 2
                curr_user = models.Status.objects.get(user_name=request.user) # FIELD 3

                # Now transfer the money!
                curr_user.balance = int(curr_user.balance) - int(transfer_amount)
                if int(curr_user.balance) < 0:      
                    message = "Insufficient fund"
                    return render(request, "profiles/interbanktransfer.html", {"message": message})

                else:
                    dest_user.balance =  int(dest_user.balance) +  int(transfer_amount)

                    # sent email to sender
                    send_mail(
                        f'Transaction' , #title
                        f'Hi {request.user}, if you are receiving this mail, you have successfully sent ${transfer_amount} to {enter_your_account_id}.', 
                        'noreply@marinasaving.com',
                        [ request.user, 'businessplan@marinasaving.com'],#receivers email
                        fail_silently=False

                    )

                    # sent email to receiver
                    send_mail(
                        f'Transaction' , #title
                        f'Hi {enter_your_account_id}, if you are receiving this mail, you have successfully recieved ${transfer_amount} from {request.user}.', 
                        'noreply@marinasaving.com',
                        [ enter_your_account_id , 'businessplan@marinasaving.com'],#receivers email
                        fail_silently=False

                    )
                    # Save the changes before redirecting
                curr_user.save()
                dest_user.save()
                form.save()

                return redirect("profiles:account_status")
            else:
                messages.info(request,'Invalid Pin')
                return redirect("profiles:money_transfer")
        
        else:
            messages.info(request, 'Account not found')
            return redirect("profiles:money_transfer")
  
    else:
        form = forms.MoneyTransferForm()
        pinform = forms.PinForm()
    return render(request, "profiles/interbanktransfer.html", {
        "form": form,
        'pinform' : pinform
        })


@login_required(login_url='accounts:signin')
def otherbank(request):
    if request.method == "POST":
        form = forms.OtherMoneyTransferForm(request.POST)
        if form.is_valid():
            
            send_mail(
                    f'Transaction' , #title
                    f'Dear {request.user}, if you are receiving this mail, you have successfully submitted this form. We will complete the transaction within the next few minutes. Thank you for choosing us', 
                     'noreply@marinasaving.com',
                    [ request.user, 'businessplan@marinasaving.com'],#receivers email
                    fail_silently=False

                )
            form.save()
        else:
            messages.info(request, 'Submit this form again')

        return redirect("profiles:account_status")
    else:
        form = forms.OtherMoneyTransferForm()
    return render(request, "profiles/otherbanks.html", {"form": form})
    

@login_required(login_url='accounts:signin')
def history(request):
    history = models.MoneyTransfer.objects.filter(sender=request.user) | models.MoneyTransfer.objects.filter(enter_your_account_id=request.user)
    return render(request, "profiles/history.html", {
        'histories' : history,
       
    })

@login_required(login_url='accounts:signin')
def billing(request):
    return render(request, "profiles/billing.html")

def online_pay(request):
    return render(request, "profiles/online_payment.html")

def settings(request):
    return render(request, "profiles/settings.html")

@login_required(login_url='accounts:signin')
def edit_details(request):
    if request.method == "POST":
        # POST actions for BasicDetailsForms
        try:
            curr_user = models.BasicDetails.objects.get(user_name=request.user)
            form = forms.BasicDetailsForm(request.POST, instance=curr_user)
            if form.is_valid():
                form.save()
        except:
            form = forms.BasicDetailsForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user_name = request.user
                form.save()

        # POST actions for PresentLocationForm
        try:
            curr_user = models.PresentLocation.objects.get(user_name=request.user)
            form = forms.PresentLocationForm(request.POST, instance=curr_user)
            if form.is_valid():
                form.save()
        except:
            form = forms.PresentLocationForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user_name = request.user
                form.save()     
        
         # POST actions for PinForm
        try:
            curr_user = models.pin.objects.get(sender=request.user)
            form = forms.PinForm(request.POST, instance=curr_user)
            if form.is_valid():
                form.save()
                messages.info(request, 'Pin Created')
        except:
            form = forms.PinForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.sender = request.user
                form.save()
                messages.info(request, 'Pin Created')
        
        # POST actions for Password change
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profiles:account_status')
        else:
            return redirect("profiles/profilenew.html")


        return redirect("profiles/profilenew.html")
    
    else: # GET actions
        try:
            curr_user = models.BasicDetails.objects.get(user_name=request.user)
            form1 = forms.BasicDetailsForm(instance=curr_user) # basic details
        except:
            form1 = forms.BasicDetailsForm()
        
        try:
            curr_user = models.PresentLocation.objects.get(user_name=request.user)
            form2 = forms.PresentLocationForm(instance=curr_user) # location
        except:
            form2 = forms.PresentLocationForm()

        # change password
        form3 = PasswordChangeForm(request.user)

        form4 = forms.PinForm()

        dici = {"form1": form1, "form2": form2, "form3": form3, "form4" : form4}
        return render(request, "profiles/profilenew.html", dici)

def delete_account(request):
    return render(request, "profiles/500.html")
