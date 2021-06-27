from django.contrib import admin
from .models import Remember


class RememberAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Remember, RememberAdmin)

