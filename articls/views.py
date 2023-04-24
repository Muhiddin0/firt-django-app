from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Article
from django.urls import reverse_lazy

# mixens
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 


# Create your views here.
class ArticlListView(ListView):
    
    model = Article
    template_name = "artikle_list.html"
    
class ArticlDetailsView(DetailView):
    
    model = Article
    template_name = "articl_details.html"
    
class ArticlUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
    model = Article
    fields = ('title','summary', 'body', 'photo')
    template_name = "articl_update.html"
    
    def get_success_url(self):
        return reverse_lazy("articl_details", kwargs={'pk': self.object.pk})

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


        
class ArticlDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    
    model = Article
    template_name = "articl_delete.html"
    success_url = reverse_lazy('articl_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticlNewView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    
    model = Article
    template_name = 'articl_new.html'
    fields = ('title','summary', 'body', 'photo',)

    def get_success_url(self):
        return reverse_lazy("articl_details", kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser
