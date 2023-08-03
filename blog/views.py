from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.


def home(request):
    cats = Category.objects.all()
    recent_post = Post.objects.all()[::-1]
    allpost = Post.objects.all()

    data = request.GET.get('category')
    if data is not None:
        cat_data = Post.objects.filter(category=data)
        context = {'cat': cats, 'allpost': allpost, 'cat_data': cat_data}
        return render(request, 'categories.html', context=context)

    context = {'cat': cats, 'post': recent_post,
               'allpost': allpost}
    return render(request, 'index.html', context=context)


def blogpost(request, slug):
    cats = Category.objects.all()
    allpost = Post.objects.all()[::-1]
    Bpost = Post.objects.filter(slug=slug)
    comm = Comment.objects.all()
    if request.method == "POST":
        msg = request.POST.get('comment_msg')
        postid = request.POST.get('postid')

        post_data = Post.objects.filter(slug=postid)

        post_com = Comment(message=msg)
        messages.success(request, 'Your comment has been posted!')
        post_com.save()

    context = {'cat': cats, 'Bpost': Bpost, 'comm': comm, 'allpost': allpost}
    return render(request, 'blogpost.html', context=context)


def contact(request):
    cats = Category.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']

        contact_obj = Contact(name=name, email=email, phone=phone, msg=msg)
        messages.success(request, "Your form has been submitted Successfully")
        contact_obj.save()
    context = {'cat': cats}

    return render(request, 'contact.html', context=context)


def search(request):
    search = request.GET['search']
    search_title = Post.objects.filter(title__icontains=search)
    search_text = Post.objects.filter(text__icontains=search)
    allpost = search_title.union(search_text)

    return render(request, 'search.html', {'search': allpost})


# def comment(request):
#     cats = Category.objects.all()
#     allpost = Post.objects.all()[::-1]
#     if request.user.is_authenticated:
#         user = request.user
#         comm = Comment.objects.filter(user=user)

#     context = {'cat': cats, 'comm': comm, 'allpost': allpost}
#     return render(request, 'blogpost.html', context=context)


def signup_page(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        pass1 = request.POST['pass1']
        cpass = request.POST['cpass']

        user_obj = User.objects.create(username=username, email=email,
                                       password=pass1)
        if len(pass1) < 5:
            messages.success(
                request, 'Password lenght should be 5 characters more!')
            return redirect('/signup')
        if pass1 != cpass:
            messages.success(request, "Password does not match!")
            return redirect('/signup')

        user_obj.save()
        messages.success(
            request, "You account has been created, now you login!")
        return redirect('login')
    return render(request, 'signup.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfully!')
            return redirect('/')
        else:
            messages.success(request, 'Sorry please enter valid details!')
            return redirect('/login')

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')
