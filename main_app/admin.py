from django.contrib import admin
from .models import Composer, Show, Favorite

# Register your models here.
admin.site.register(Composer)
admin.site.register(Show)
admin.site.register(Favorite)