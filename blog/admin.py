from django.contrib import admin
from .models import TipoUsuario, Post

# Register your models here.
class TipoUsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(TipoUsuario, TipoUsuarioAdmin)
admin.site.register(Post, PostAdmin)