"""secondapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blogs.urls")),
    path('login/', include("blogs.urls")),
    path('clogin/<title>/', include("blogs.urls")),
    path('logout/', include("blogs.urls")),
    path('admin_logout/', include("blogs.urls")),
    path('profile/<int:id>/', include("blogs.urls")),
    path('admin_profile/<int:aid>/', include("blogs.urls")),
    path('delete/<int:id>/<int:aid>/', include("blogs.urls")),
    path('update/<int:id>/<int:aid>/', include("blogs.urls")),
    path('register/', include("blogs.urls")),
    path('save_blog/<int:id>/', include("blogs.urls")),
    path('back/<int:id>/', include("blogs.urls")),

    path('directly_verify_user/<int:author_id>/', include("blogs.urls")),
    path('add_comment/<int:id>/<title>/', include("blogs.urls")),
    path('add_comment_in_author_blog/<int:user_id>/<title>/<int:id>/', include("blogs.urls")),
    path('show_author_comments/<int:id>/', include("blogs.urls")),
    path('delete_blog/<int:id>/<title>/', include("blogs.urls")),
    path('edit_blog/<int:id>/<title>/<int:blog_id>/', include("blogs.urls")),
    path('delete_blog_user/<title>/<int:id>/', include("blogs.urls")),
    path('blog/<int:id>/', include("blogs.urls")),
    path('show_blog/', include("blogs.urls")),
    path('show_comment/', include("blogs.urls")),
    path('verification_author/<int:id>/', include("blogs.urls")),
    path('admin_login/', include("blogs.urls")),
    path('author_blogs/<int:id>/', include("blogs.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
