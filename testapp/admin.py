from django.contrib import admin
from testapp.models import Blood_Donner_Model, Updates_Table


class Admin_Blood_Decide(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Mobile', 'Address', 'Blood_Group', 'Last_Donation_Date', 'Date_O_Birth']


class Admin_Update(admin.ModelAdmin):
    list_display = ['Next_Camp_Address', 'Camp_Date', 'Timing_from']


admin.site.register(Blood_Donner_Model, Admin_Blood_Decide)
admin.site.register(Updates_Table, Admin_Update)

