from django.shortcuts import render
from .models import News, Category


def home(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'title': 'Main Page',
        'news': news,
        'categories': categories
    }
    return render(request, 'blog/home.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'categories': categories,
        'category': category
    }
    return render(request, 'blog/category.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'О клубе Python Bytes'})
