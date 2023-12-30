from django.utils.text import slugify
from django.db import models

from model_utils.models import TimeStampedModel


class Article(TimeStampedModel):
    title = models.CharField(
        name="title", max_length=73, help_text="Enter the article title", null=True
    )
    description = models.TextField(
        name="description", help_text="Enter text", null=True
    )
    image = models.ImageField(
        name="image", help_text="Upload cover image", blank=True, null=True
    )
    slug = models.SlugField(
        name="slug", auto_created=True, unique=True, blank=True, null=True
    )

    class Meta:
        ordering = ("-id",)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
