from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    data = {'news': Article.objects.all()}
    return render(request, 'news/news_home.html', data)


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма заполнена неккоректно!'
    form =  ArticleForm()
    data = {
        'form': form,
        'error':error
    }
    return render(request, 'news/create.html', data)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'news/detail_view.html'
    context_object_name = 'article'

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'news/create.html'

    form_class = ArticleForm

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = '/news/'
    template_name = 'news/delete.html'