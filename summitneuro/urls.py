"""
URL configuration for summitneuro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from summitneuro.sitemaps import BlogSitemap, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from core.views import serve_media

sitemaps = {
    "blog": BlogSitemap,
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("user/", include("userauths.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    re_path(r"^media/(?P<path>.*)$", serve_media),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)