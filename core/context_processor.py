from core.models import Blog

def default(request):
    list_blogs = Blog.objects.filter(is_active=True).order_by("-created_at").all()[:3]
    
    return {
        "blogs": list_blogs,
    }