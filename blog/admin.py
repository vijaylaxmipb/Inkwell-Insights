from django.contrib import admin
from .models import Post, Comment, Contact
from .models import Contact, DevProfile


# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.register(Contact)  
admin.site.register(DevProfile)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'status')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')

class ContactAdmin(admin.ModelAdmin):
    """Allows admin to manage user contacts via the admin panel"""
    list_display = ['email', 'subject', 'created_on']