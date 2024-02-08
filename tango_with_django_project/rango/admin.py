from django.contrib import admin
from rango.models import Category, Page

# Register your models here.


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'Category', 'url']
    
   
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','likes','views']
    
admin.site.register(Category, CategoryAdmin)



