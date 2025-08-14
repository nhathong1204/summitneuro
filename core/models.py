import uuid
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify

def user_directory_path(instance, filename):
    unique_filename = f"{instance.owner.id}-{filename}"
    return f"user_{instance.owner.id}/{unique_filename}"


class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="blog", null=True, blank=True, on_delete=models.SET_NULL
    )
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    description = RichTextUploadingField(null=True, blank=True)
    mini_description = models.TextField(default=None, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


    def get_absolute_url(self):
        return reverse("core:blog-detail", args=[str(self.slug)])

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class ContactUs(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = "ContactUs"
        verbose_name_plural = "ContactUs"

    def __str__(self) -> str:
        return self.email