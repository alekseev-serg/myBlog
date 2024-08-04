from django.shortcuts import render
from .models import News, Category


def home(request):
    news = News.objects.all()
    context = {
        'title': 'Main Page',
        'news': news,
    }
    return render(request, 'blog/home.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category
    }
    return render(request, 'blog/category.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'О клубе Python Bytes'})
