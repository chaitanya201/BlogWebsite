from django.shortcuts import render

# Create your views here.


from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from .models import userDetails, Blogs, Comments


def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        u_email=request.POST['email']
        pass1=request.POST['password']
        pass2=request.POST['cpassword']
        if pass1==pass2:
            print("Email is ", userDetails.objects.filter(email=u_email))
            if not userDetails.objects.filter(email=u_email).exists():
                user=userDetails(name=name,email=u_email,password=pass2)

                user.save()
                return render(request,'login.html')

            else:
                return render(request,'register.html',{'error':'mail is already used'})
        else:
            return render(request,'register.html',{'error':'Enter same Password'})
    else:
        return render(request,'register.html')

def log_in(request):
    if request.method=='POST':
        email=request.POST['email']
        pass1=request.POST['password']
        print('the request is ',request)
        if userDetails.objects.filter(email=email,password=pass1):

            for obj in userDetails.objects.filter(email=email):
                if obj.email==email:
                    user_id=obj.id
                    name=obj.name
                    profile_photo=obj.profile
                    break

            all_blogs=Blogs.objects.all()
            #user = userDetails(id=user_id)
            #login(request,user)
            return render(request,'profile.html',{'name':name,'id':user_id,"blog":all_blogs,'profile_photo':profile_photo})
        else:
            return render(request,'login.html',{'error':'Enter valid details'})
    else:
        return render(request,'login.html')

def log_out(request):
    print("This is home page")
    logout(request)
    return redirect('/')

def profile(request,id):
    for obj in userDetails.objects.filter(id=id):
        if obj.id==id:
            name=obj.name

    all_blogs=Blogs.objects.all()
    print("all blogs are  ",all_blogs)

    return render(request,'profile.html',{'id':id,'name':name,'blog':all_blogs})

def blog(request,id):
    return render(request,'blogs.html',{'id':id})

def admin_login(request):
    if request.method=='POST':
        user_name=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=user_name, password=password)
        if user:
            login(request,user)
            name=request.user
            print(user.id)
            print("name is ", name)
            print()
            all_blogs=Blogs.objects.all()
            all_data=userDetails.objects.all()

            return render(request,'admin profile.html',{'name':name,'all_data':all_data,'aid':user.id,'all_blogs':all_blogs})
        else:
            form = AuthenticationForm()
            return render(request,'admin login.html',{'error':'Enter valid username or Password'}, {'form': form})
    else:
        form=AuthenticationForm()
        return render(request,'admin login.html', {'form': form})


def delete_blog_admin(request,id,title):
    blog = Blogs.objects.get(title=title)
    blog.delete()
    name=User.objects.get(id=id)
    all_blogs=Blogs.objects.all()
    all_users=userDetails.objects.all()
    return render(request,'admin profile.html',{'all_blogs':all_blogs,'all_data':all_users,'name':name,'title':title,'aid':id})


def delete_blog_user(request,title,id):
    blog_delete=Blogs.objects.get(title=title)
    blog_delete.delete()
    user=userDetails.objects.get(id=id)
    name=user.name
    all_blogs=Blogs.objects.all()
    return render(request,'profile.html',{'title':title,'id':id,'name':name,'blog':all_blogs})


def admin_logout(request):
    logout(request)
    return redirect('/')


def del_student(request,id,aid):
    user=userDetails(id=id)
    user.delete()
    data=userDetails.objects.all()
    return render(request,'admin profile.html',{'all_data':data,'id':id,'aid':aid})


def update(request,id,aid):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        email=request.POST['email']
        user=userDetails(id=id,name=name,password=password,email=email)
        user.save(update_fields=(['name','password','email']))
        for i in User.objects.all():
            if i.id==aid:
                name=i.first_name
                break
        all_blogs=Blogs.objects.all()
        all_users=userDetails.objects.all()
        return render(request,'admin profile.html',{'id':id,'name':name,'all_blogs':all_blogs,'all_data':all_users,'aid':aid})
    else:
        user=userDetails.objects.filter(id=id)

        #print('user details are ',user.id,user.name,user.email)
        return render(request,'update.html',{'id':id,'user':user,'aid':aid})


def save_blog(request, id):
    if request.method=='POST':
        title=request.POST['heading']
        content=request.POST['blog']
        user_object = userDetails.objects.get(id=id)
        if Blogs.objects.filter(title=title):
            return render(request,'blogs.html',{'id':id,'msg':'Blog Title is already taken, Try something New..'})
        else:

            if request.FILES['img1']:
                img1=request.FILES['img1']
                Blogs.objects.create(title=title, blog_content=content, user_blog=user_object, img1=img1)
            elif request.FILES['img2']:
                img2=request.FILES['img2']
                Blogs.objects.create(title=title, blog_content=content, user_blog=user_object, img2=img2)
            else:
                img1 = request.FILES['img1']
                img2 = request.FILES['img2']
                Blogs.objects.create(title=title, blog_content=content, user_blog=user_object, img1=img1,img2=img2)
            print("user id with object is this ",user_object)
            print('blog is saved!!!')
            return render(request,'blogs.html',{'success':"Blog is uploaded Successfully!!!!",'id':id})
    else:
        return render(request,'blogs.html', {'id': id})


def show_author_blogs(request, id):

    all_blogs=Blogs.objects.filter(user_blog_id=id)
    author=userDetails.objects.get(id=id)
    name=author.name
    profile_pic=author.profile
    return render(request,'show author blogs.html',{'id':id,'name':name,'all_blogs':all_blogs,'profile_pic':profile_pic})


def show_author_comments(request,id):
    all_blogs=Blogs.objects.filter(user_blog_id=id)
    all_comments=Comments.objects.all()
    author=userDetails.objects.get(id=id)
    name=author.name
    profile=author.profile
    return render(request,'show author comments.html',{'all_blogs':all_blogs,'all_comments':all_comments,'name':name,'profile_pic':profile,'id':id})


def back(request,id):
    user=userDetails.objects.filter(id=id)
    for i in user:
        if i.id==id:
            name=i.name
            break
            print(user,'this is is ',i.name)
    all_blogs=Blogs.objects.all()
    profile_photo=userDetails.objects.get(id=id).profile

    return render(request,'profile.html',{'id':id,'blog':all_blogs,'name':name,'profile_photo':profile_photo})


def show_blogs(request):
    all_blogs=Blogs.objects.all()
    all_users=userDetails.objects.all()
    return render(request,'show blogs.html',{'all_blogs':all_blogs,'all_users':all_users})


def verify(request,id):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if userDetails.objects.filter(email=email,password=password):
            all_blogs=Blogs.objects.all()
            all_comments=Comments.objects.all()
            user=userDetails.objects.get(id=id)
            name=user.name
            profile=user.profile
            user1=userDetails.objects.get(email=email)
            user_id=user1.id
            return render(request,'comment in author blogs.html',{'id':id,'name':name,'all_comments':all_comments,'all_blogs':all_blogs,'profile_pic':profile,'user_id':user_id})
        else:
            return render(request,'verify.html',{"msg":'Enter Valid Details',"id":id})

    else:
        return render(request, 'verify.html', {"id": id})


def add_comment_in_author_blog(request,user_id,title,id):
    if request.method == 'POST':
        comment=request.POST['comment']
        com_obj=Comments(user_comment_id=user_id,blog_title=title,comment=comment)
        com_obj.save()
        all_comments=Comments.objects.all()
        all_blogs=Blogs.objects.all()
        user=userDetails.objects.get(id=id)
        name=user.name
        profile=user.profile
        return render(request,'comment in author blogs.html',{'id':id,'name':name,'all_comments':all_comments,'all_blogs':all_blogs,'profile_pic':profile,'user_id':user_id})
    else:
        return render(request,'comment in author blogs.html',{'id':id,'user_id':user_id,'title':title})

def directly_add_comment_author(request):
    pass
def direct_verify(request,id):
    if request.method=='POST':
        email=request.POST['email']
        passwod=request.POST['password']
        if userDetails.objects.filter(email=email,password=passwod):
            all_blogs=Blogs.objects.filter(user_blog_id=id)
            all_comments=Comments.objects.all()
            author=userDetails.objects.get(id=id)
            name=author.name
            profile=author.profile
            user1=userDetails.objects.get(email=email)
            user_id=user1.id

            return render(request,'author directly add comments.html',
                          {
                              'author_id':id,'all_blogs':all_blogs,"all_comments":all_comments,'name':name,'profile_pic':profile,'user_id':user_id
                          })
        else:
            return render(request,'directly verify.html',{'id':id,'msg':'Enter Valid Details'})
    else:
        return render(request,'directly verify.html',{'id':id})


def user_profile_photo(request,id):
    if request.method=='POST':
        img=request.FILES['profile_photo']
        user=userDetails(profile=img,id=id)
        user.save(update_fields=['profile'])

        # noinspection PyUnreachableCode
        user_obj=userDetails.objects.get(id=id)
        name = user_obj.name
        profile_photo=user_obj.profile

        all_blogs = Blogs.objects.all()
        print("all blogs are  ", all_blogs)

        return render(request, 'profile.html', {'id': id,'name': name, 'blog': all_blogs,'profile_photo':profile_photo})
    else:
        user_obj = userDetails.objects.get(id=id)
        name = user_obj.name
        profile_photo = user_obj.profile

        all_blogs = Blogs.objects.all()
        print("all blogs are  ", all_blogs)

        return render(request, 'profile.html',
                      {'id': id, 'name': name, 'blog': all_blogs, 'profile_photo': profile_photo})


def edit_blog(request, id, title, blog_id):
    if request.method=='POST':
        title = request.POST['title']
        content = request.POST.get('blog')
        print(content)
        user_object = userDetails.objects.get(id=id)
        blog_obj=Blogs.objects.get(title=title)
        if request.FILES.get('img1'):
            if request.FILES.get('img2'):
                img2=request.FILES.get('img1')
            else:
                img2=None
            img1 = request.FILES['img1']
            blog_obj=Blogs(id=blog_id, title=title, blog_content=content, user_blog_id=id, img1=img1,img2=img2)
            blog_obj.save(update_fields=['title', 'blog_content', 'img1', 'img2', 'time'])
        elif request.FILES.get('img2'):
            img2 = request.FILES['img2']
            if request.FILES.get('img1'):
                img1=request.FILES.get('img1')
            else:
                img1=None
            #b = Blogs.objects.get(pk=id)
            #print('b is  ', b)
            #Blogs.objects.filter(pk=blog_id).update(user_blog=b)
            blog_obj = Blogs(id=blog_id, title=title, blog_content=content, user_blog_id=id, img2=img2,img1=img1)
            blog_obj.save(update_fields=['title', 'blog_content', 'img1', 'img2', 'time'])
        elif request.FILES.get('img1') and request.FILES.get('img2'):
            img1 = request.FILES['img1']
            img2 = request.FILES['img2']
            #b=Blogs.objects.get(pk=id)
            #print('b is  ',b)
            #Blogs.objects.filter(pk=blog_id).update(user_blog=b)
            blog_obj = Blogs(id=blog_id, title=title, blog_content=content, user_blog_id=id, img1=img1,img2=img2)
            blog_obj.save(update_fields=['title', 'blog_content', 'img1', 'img2', 'time'])
        else:
            if blog_obj.img1:
                img1=blog_obj.img1
            else:
                img1=None
            if blog_obj.img2:
                img2=blog_obj.img2
            else:
                img2=None
            blog_obj = Blogs(id=blog_id, title=title, blog_content=content, user_blog_id=id,img1=img1,img2=img2)
            blog_obj.save(update_fields=['time'])

        all_blogs = Blogs.objects.get(user_blog_id=id, title=title)
        return render(request,'edit blog.html', {'msg': 'Blog is updated successfully!!!','id':id,'title':title,'blog_id':blog_id,'blog':all_blogs})
    else:
        all_blogs=Blogs.objects.get(user_blog_id=id,title=title)

        return render(request,'edit blog.html',{'id':id,'title':title,'blog':all_blogs,'blog_id':blog_id})


def admin_profile(request,aid):
    all_data=userDetails.objects.all()
    for i in User.objects.all():
        if i.id==aid:
            name=i.first_name
    all_blogs=Blogs.objects.all()
    return render(request,'admin profile.html',{'all_data':all_data,'name':name,'aid':aid,'all_blogs':all_blogs})


def comment_login(request,title):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if userDetails.objects.filter(email=email,password=password):
            for i in userDetails.objects.filter(email=email,password=password):
                if i.email==email:
                    id=i.id
                    break
                else:
                    id=-1
            all_blogs=Blogs.objects.all()
            all_comments=Comments.objects.all()
            all_users=userDetails.objects.all()
            print('all blogs',all_blogs,'all comments',all_comments)
            return render(request,'comment in bog.html',{'id':id,'title':title,'all_blogs':all_blogs,'all_comments':all_comments,'all_users':all_users})
        else:
            return render(request,'comments.html',{'error':'Please enter Valid details','title':title})
    else:
        return render(request,'comments.html',{'title':title})

def add_comment(request,id,title):
    if request.method=='POST':
        comment=request.POST['comment']
        user=Comments.objects.create(comment=comment,blog_title=title,user_comment_id=id)
        user.save()
        all_comments = Comments.objects.all()
        all_users=userDetails.objects.all()
        all_blogs=Blogs.objects.all()
        return render(request, 'comment in bog.html',
                      {'all_comments': all_comments,'all_users':all_users,
                       "all_blogs":all_blogs,'id':id,'title':title
                       })
    else:
        return render(request,'comment in bog.html',{'id':id,'title':title})


def show_comments(request):
    all_users=userDetails.objects.all()
    all_data=Comments.objects.all()
    all_blogs=Blogs.objects.all()
    print(all_users)
    return render(request,'show comments.html',{'all_comments':all_data,
                                                'all_users':all_users,'all_blogs':all_blogs
                                                })


