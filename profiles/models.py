from django.db import models
from django.contrib.auth.models import User

class BasicDetails (models.Model):
    # (Name, Sex, DOB, Annual income, Email, Mobile number, Occupation) 
    name            = models.CharField(max_length = 50, default = None)
    sex             = models.CharField(max_length = 1, default = None)
    annual_income   = models.IntegerField(default = 0)
    email           = models.EmailField(default = None)
    mobile          = models.IntegerField(default = 0)
    occupation      = models.CharField(max_length = 50, default = None)
    DOB             = models.DateField(default = None)
    user_name       = models.CharField(max_length = 150, default = None)
    BVN             = models.CharField(max_length = 50, default = None, null=True )
    National_ID     = models.CharField(max_length = 50, default = None, null=True)
    ID_number       = models.CharField(max_length = 50, default = None, null=True)



    class Meta:
        verbose_name = 'User Information'
        verbose_name_plural = 'User Informations'

class PresentLocation (models.Model):
    # (Country, State, City, Street, Pincode) 
    country = models.CharField(max_length = 50, default = "India")
    state = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    street = models.CharField(max_length = 50)
    pincode = models.IntegerField()
    user_name = models.CharField(max_length = 150, default = None)

class Status (models.Model):
    account_number = models.IntegerField()
    balance = models.IntegerField()
    user_name = models.CharField(max_length = 150, default = None)

    class Meta:
        verbose_name = 'Account detail'
        verbose_name_plural = 'Account details'


class MoneyTransfer(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    enter_your_account_id = models.CharField(max_length = 150, default = None)
    enter_the_destination_account_number = models.IntegerField()
    enter_the_amount_to_be_transferred= models.IntegerField()

    class Meta:
        verbose_name = 'Inter bank transfer'
        verbose_name_plural = 'Inter bank transfers'

class OtherTransfer(models.Model):
    enter_your_bank = models.CharField(max_length = 150, default = None)
    enter_your_account_name = models.CharField(max_length = 150, default = None)
    enter_the_destination_account_number = models.IntegerField()
    enter_the_amount_to_be_transferred= models.IntegerField( null=True)

    class Meta:
        verbose_name = 'Other bank transfer'
        verbose_name_plural = 'Other bank transfers'

class pin(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='senderpin')
    pin   = models.IntegerField(max_length=4)



