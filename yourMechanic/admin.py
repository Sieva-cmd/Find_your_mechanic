from django.contrib import admin
from .models import Engine, Customer, User

# Register your models here.
admin.site.register(User)
admin.site.register(Engine)
admin.site.register(Customer)


