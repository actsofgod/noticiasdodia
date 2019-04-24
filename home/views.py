from django.shortcuts import render
from .utils import get_globo_posts, get_meiahr_posts

# Create your views here.
def home(request):
    template = 'home/index.html'
    globo_posts = get_globo_posts()
    meiahr_posts = get_meiahr_posts()
    context = {'globo_posts': globo_posts, 'meiahr_posts': meiahr_posts}
    return render(request, template, context)
