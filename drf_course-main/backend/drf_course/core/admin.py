from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAd min):
    list_display = ('id', 'title', 'description', 'email')