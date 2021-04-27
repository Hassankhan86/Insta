from django.contrib import admin

# Register your models here.
from accounts.models import Account,Profile

admin.site.register(Account)
admin.site.register(Profile)