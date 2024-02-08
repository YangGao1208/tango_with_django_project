from django.contrib import admin
from rango.models import Category, Page

# Register your models here.


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'Category', 'url']
    


admin.site.register(Category)



