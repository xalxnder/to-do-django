from django.contrib import admin
from .models import ToDos

# Register your models here.


class ToDosAdmin(admin.ModelAdmin):
    readonly_fields = ('created')


admin.site.register(ToDos)
