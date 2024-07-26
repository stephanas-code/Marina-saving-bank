from django import forms
from . import models

class BasicDetailsForm (forms.ModelForm):
    # class to store all the model form fields from models.py
    class Meta:
        model = models.BasicDetails
        fields = ["name", "sex", "DOB", "annual_income", "email", "mobile", "occupation", "BVN", 'National_ID', "ID_number"]


class PresentLocationForm (forms.ModelForm):
    class Meta:
        model = models.PresentLocation
        fields = ["country", "state", "city", "street", "pincode"]

class MoneyTransferForm (forms.ModelForm):
    class Meta:
        model = models.MoneyTransfer
        fields = [
            "enter_your_account_id",
            "enter_the_destination_account_number", 
            "enter_the_amount_to_be_transferred"
        ]

class OtherMoneyTransferForm (forms.ModelForm):
    class Meta:
        model = models.OtherTransfer
        fields = [
            "enter_your_bank",
            "enter_your_account_name",
            "enter_the_destination_account_number", 
            "enter_the_amount_to_be_transferred"
        ]

class PinForm(forms.ModelForm):
    class Meta:
        model = models.pin
        fields =['pin']
