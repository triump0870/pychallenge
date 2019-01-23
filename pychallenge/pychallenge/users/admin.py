from django.contrib import admin
from .models import About
from markdownx.admin import MarkdownxModelAdmin


# Register your models here.

admin.site.register(About, MarkdownxModelAdmin)
