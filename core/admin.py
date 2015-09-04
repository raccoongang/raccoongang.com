from django.contrib import admin
from .models import Block


class CallToActionAdmin(admin.ModelAdmin):
    list_display = ('title', 'button_title', 'button_link')


admin.site.register(Block, CallToActionAdmin)


# Register your models here.
