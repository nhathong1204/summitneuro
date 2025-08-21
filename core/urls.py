from django.urls import path
from core import views

app_name = "core"
urlpatterns = [
    path("", views.index, name="index"),
    path("dr-gary/", views.doctor_detail, name="dr-gary"),
    path("blogs/", views.list_blogs, name="blogs"),
    path("blogs/<str:slug>/", views.blog_detail, name="blog-detail"),
    path("contact-us/", views.contact_us, name="contact-us"),
    path("ajax-contact-form", views.ajax_contact_form, name="ajax-contact-form"),
]
