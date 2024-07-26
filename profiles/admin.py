from django.contrib import admin
from .models import *


admin.site.site_header ='FINA BANK ADMIN'
admin.site.site_title ='FINA BANK ADMIN PORTAL'
admin.site.index_title='WELCOME TO FINA BANK ADMIN PORTAL'

class BasicDetailsSite(admin.ModelAdmin):
    model = BasicDetails    

    list_display =('name', 'email', 'mobile', 'DOB')

    list_filter = ['name', 'email',]

    search_fields = ['name', 'occupation',]

class PresentLocationSite(admin.ModelAdmin):
    model = PresentLocation    

    list_display =('user_name','country', 'state',)

    list_filter = ['user_name','country', 'state',]

    search_fields = ['user_name','country', 'state',]  

class StatusSite(admin.ModelAdmin):
    model = PresentLocation    

    list_display =('user_name','account_number', 'balance',)

    list_filter = ['user_name','account_number', 'balance',]

    search_fields = ['user_name','account_number', 'balance',]  


class MoneyTransferSite(admin.ModelAdmin):
    model = MoneyTransfer    

    list_display =('sender','enter_your_account_id', 'enter_the_destination_account_number',)

    list_filter = ['sender','enter_your_account_id', 'enter_the_destination_account_number',]

    search_fields = ['sender','enter_your_account_id', 'enter_the_destination_account_number',]  
  

class OtherTransferSite(admin.ModelAdmin):
    model = OtherTransfer    

    list_display =('enter_your_account_name','enter_your_bank', 'enter_the_destination_account_number',)

    list_filter = ['enter_your_account_name','enter_your_bank', 'enter_the_destination_account_number',]

    search_fields = ['enter_your_account_name','enter_your_bank', 'enter_the_destination_account_number',]  


admin.site.register(BasicDetails, BasicDetailsSite)
admin.site.register(PresentLocation, PresentLocationSite)
admin.site.register(Status, StatusSite)
admin.site.register(MoneyTransfer, MoneyTransferSite)
admin.site.register(OtherTransfer, OtherTransferSite)
admin.site.register(pin)


