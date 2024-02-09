from django.db import models
from django.template.defaultfilters import slugify



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 128, unique = True)
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    slug = models.SlugField()
    class Meta:
        verbose_name_plural = "Categories"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        
    
    def __str__(self):
        return self.name
    

class Page(models.Model):
    Category = models.ForeignKey(Category, on_delete = models.CASCADE)
    title = models.CharField(max_length = 128)
    url = models.URLField()
    views = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.title
    

# class PageForm(forms.ModelForm):
#     def clean(self):
#         cleaned_data = self.cleaned_data
#         url = cleaned_data.get('url')
        
#         if url and not url.startswitch('http://'):
#             url = f'http://{url}'
#             cleaned_data['url'] = url
            
#         return cleaned_data
            
            
