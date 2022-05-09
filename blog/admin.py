from django.contrib import admin

# Register your models here.

from .models import BlogPost

admin.site.register(BlogPost)


# from django.contrib.auth.admin import UserAdmin
# from .models import User

# admin.site.register(User, UserAdmin)