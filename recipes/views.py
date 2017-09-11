from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import RecipePost
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm


def index(request):
    posts = RecipePost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 10)
    try:
    	users = paginator.page(page)
    except PageNotAnInteger:
    	users = paginator.page(1)
    except EmptyPage:
    	users = paginator.page(paginator.num_pages)

    return render(request, 'index.html', { 'posts': posts })

def post_detail(request, pk):
    post = get_object_or_404(RecipePost, pk=pk)
    return render(request, 'detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'post_edit.html', {'form': form})