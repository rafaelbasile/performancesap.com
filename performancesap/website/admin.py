from django.contrib import admin

# Register your models here.
from .models import ContactM

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'content')
    exclude = ('active',)

admin.site.register(ContactM, PostAdmin)
