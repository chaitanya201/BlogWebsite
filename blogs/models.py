from django.db import models

# Create your models here.
class userDetails(models.Model):
    name = models.TextField(max_length=40)
    email = models.EmailField()
    password=models.TextField(max_length=20)
    profile=models.ImageField(upload_to='blog_user_profile',null=True, blank=True)
    """
    title=models.CharField(max_length=200,default='No Title')
    blog=models.TextField(max_length=10000,default='No Title')
    comment=models.TextField(max_length=1000,default='No Comments')
    """
    class Meta:
        db_table="User Details"

    def __str__(self):
        return self.name


class Blogs(models.Model):
    title=models.CharField(max_length=200)
    blog_content=models.TextField(max_length=10200)
    user_blog=models.ForeignKey(userDetails,on_delete=models.CASCADE)
    img1=models.ImageField(upload_to='blog_images',null=True,blank=True)
    img2=models.ImageField(upload_to='blog_images',null=True,blank=True)
    time=models.DateTimeField(auto_now_add=True,null=True)
    class Meta:
        db_table="All Blogs"

    def __str__(self):
        return self.title

class Comments(models.Model):
    time=models.DateTimeField(auto_now_add=True)
    blog_title=models.TextField(max_length=200,default='No Blog Title')
    comment=models.TextField(max_length=500)
    user_comment=models.ForeignKey(userDetails,on_delete=models.CASCADE)
    class Meta:
        db_table="All Comments"

    def __str__(self):
        return self.blog_title



