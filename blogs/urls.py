from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home_page'),
    path('register/',register,name='register'),
    path('login/', log_in, name='login'),
    path('logout/',log_out,name='logout'),
    path('admin_logout/',admin_logout,name='admin_logout'),
    path('profile/<int:id>/',profile,name='profile'),
    path('admin_profile/<int:aid>/',admin_profile,name='admin_profile'),
    path('delete/<int:id>/<int:aid>/',del_student,name='delete'),
    path('update/<int:id>/<int:aid>/',update,name='update'),
    path('save_blog/<int:id>/',save_blog,name='save_blog'),
    path('back/<int:id>/',back,name='back'),
    path('author_blogs/<int:id>/',show_author_blogs,name='author_blogs'),
    path('clogin/<title>/',comment_login,name='comment_login'),
    path('profile_photo/<int:id>/',user_profile_photo,name='upload_profile_photo'),
    path('add_comment/<int:id>/<title>/',add_comment,name='add_comment'),
    path('add_comment_in_author_blog/<int:user_id>/<title>/<int:id>/',add_comment_in_author_blog,name='au_comment'),
    path('delete_blog/<int:id>/<title>/',delete_blog_admin,name='delete_blog'),
    path('show_author_comments/<int:id>/',show_author_comments,name='show_author_comments'),
    path('verification/<int:id>/',verify,name="verify"),
    path('verification_author/<int:id>/',direct_verify,name="diverify"),
    #path('directly_verify_user/<int:author_id>/',direct_verify,name="directly_verify"),

    path('edit_blog/<int:id>/<title>/<int:blog_id>/',edit_blog,name='edit_blog'),
    path('delete_blog_user/<title>/<int:id>/',delete_blog_user,name='delete_blog_user'),
    path('show_comment/',show_comments,name='show_comments'),
    path('show_blog/',show_blogs,name='show_blog'),
    path('admin_login/',admin_login,name='admin_login'),
    path('blog/<int:id>/',blog,name='blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
