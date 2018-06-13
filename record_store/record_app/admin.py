from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from record_app.models import Band, Album, Track

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Band)
admin.site.register(Album)
admin.site.register(Track)
