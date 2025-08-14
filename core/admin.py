from django.contrib import admin
from core.models import Blog, ContactUs

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "owner",
        "slug",
        "mini_description",
        "is_active",
        "created_at",
    ]
    search_fields = ["id", "title", "owner__email", "slug"]
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        js = ("ckeditor/ckeditor/ckeditor.js",)
        js += ("assets/js/ckeditor_signed_upload.js",)

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "phone", "subject"]