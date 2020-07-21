from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Ebook, Comment
from django.core.paginator import Paginator
from django.contrib import auth
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.
def homepage(request):
    ebooks = Ebook.objects.order_by('-id')[:8]
    return render(request, 'ebook/homepage.html', {
        'ebooks' : ebooks
    })

def categories_(request):
    categories = Category.objects.order_by('name')
    return render(request, 'ebook/categories_.html', {
		'categories': categories,
		})

def category_(request, category_id):
    category = get_object_or_404(Category, pk = category_id)
    ebooks = category.ebook_set.all()

    paginator = Paginator(ebooks, 4)
    try:
        page = request.GET['page']
    except:
        page = 1
    ebooks = paginator.get_page(page)

    return render(request, 'ebook/category_.html', {
		'category' : category,
		'ebooks' : ebooks
		})


def ebooks_(request):
    ebooks = Ebook.objects.all()
    paginator = Paginator(ebooks, 5)
    try:
        page = request.GET['page']
    except:
        page = 1
    ebooks = paginator.get_page(page)
    return render(request, 'ebook/ebooks_.html', {
    	'ebooks': ebooks,
    	})

def ebook(request, ebook_id):
    ebook = get_object_or_404(Ebook, pk = ebook_id)
    comments = ebook.comment_set.all()
    return render(request, 'ebook/ebook.html', {
		'ebook' : ebook,
        'comments' : comments,
		})

def ebook_(request, ebook_id):
    ebook = get_object_or_404(Ebook, pk = ebook_id)
    comments = ebook.comment_set.all()
    return render(request, 'ebook/ebook_.html', {
		'ebook' : ebook,
        'comments' : comments,
		})

def comment(request, ebook_id):
    if request.method == 'POST':
        user = auth.get_user(request)
        ebook = get_object_or_404(Ebook, pk = ebook_id)

        # create the comment
        comment = Comment()
        comment.body = request.POST['body']
        comment.pub_time = timezone.datetime.now()
        comment.ebook = ebook
        comment.user = user
        comment.save()

        return redirect('ebook_', ebook_id)
    else:
        return redirect('homepage')


#user authentication

def signup_(request):
    if request.method == 'POST':
        # sign up the user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'ebook/signup_.html', {'error': 'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return render(request, 'ebook/homepage.html', {'success': 'You are successfully registered and logged in!'})
        else:
            return render(request, 'ebook/signup_.html', {'error': 'Passwords aren\'t matched!'})
    else:
        # user wants to sign up
        return render(request, 'ebook/signup_.html')


def login_(request):
    if request.method == 'POST':
        # login user
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return render(request, 'ebook/homepage.html', {'success': 'You are successfully logged in!'})
        else:
            return render(request, 'ebook/login_.html', {'error': 'Username/Password doesn\'t match'})
    else:
        # user wants to login
        return render(request, 'ebook/login_.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('homepage')
