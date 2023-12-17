from django.utils.text import slugify 
from django.db import models

class Article(models.Model):
    title = models.CharField(name="title", max_length=73, help_text="Enter the article title", null=True)
    description = models.TextField(name="description", help_text="Enter text", null=True)
    image = models.ImageField(name="image", help_text="Upload cover image", blank=True, null=True)
    slug = models.SlugField(name="slug", auto_created=True, unique=True, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    class Meta:
        ordering = ('-created_at',)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title