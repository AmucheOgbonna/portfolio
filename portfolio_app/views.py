from django.shortcuts import render
from django.contrib.auth.models import User
from portfolio_app.models import Post,Category
 
# Create your views here.
# def index(request):
#     return render(request, 'porfolio_app/index.html')
def index(request):
    posts = Post.objects.all()
    category = Category.objects.all()
    
    args = {'post_key':posts, 'category_key':category}
    return render(request, 'portfolio_app/index.html', args)
def blog_single(request):
    posts = Post.objects.all()
    category = Category.objects.all()
    
    args = {'post_key':posts, 'category_key':category}
    return render(request, 'portfolio_app/blog-single.html', args)
