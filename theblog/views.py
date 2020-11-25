from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from taggit.models import Tag

from .models import Post, Category,Profile
from .forms import PostForm,updateForm

from urllib.parse import quote_plus

from hitcount.views import HitCountDetailView

# Create your views here.

def aboutView(request):
    return render(request,"aboutme.html",{})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #ordering = ['-post_date']
    paginate_by = 3
    #ordering = ['-id']

    count_hit = True

    def get_queryset(self):
        return Post.objects.filter(draft=False).order_by('-post_date')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        try:
            author = User.objects.get(id=1)
        except User.DoesNotExist:
            author = None
        #print(author)
        #print(profile)
        context.update({"author":author})
        return context

class DraftView(ListView):
    model = Post
    template_name = 'draftList.html'
    #ordering = ['-post_date']
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(draft=True).order_by('-publish')

class categoryListView(ListView):
    model = Category
    template_name = "categoryListView.html"

def categoryView(request,slug):
    #cats = cats.replace('-',' ').title()
    #Capital
    #category_list = Post.objects.filter(category=cats)
    listname = Category.objects.get(slug=slug)
    category_list = Post.objects.filter(Category=listname,draft=False)
    return render(request,"categoryList.html",{"cats":listname,"lists":category_list})

class articleDetailView( HitCountDetailView,DetailView):
    model = Post
    template_name = "articleDetail.html"
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(articleDetailView, self).get_context_data(**kwargs)
        self.object = self.get_object()
        similar_posts = self.object.tags.similar_objects()[:3]
        try:
            author = User.objects.get(id=1)
        except User.DoesNotExist:
            author = None
        context.update({"share_string":quote_plus(self.object.body),"similar":similar_posts,"author": author})
        return context

class addArticleView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "addBlog.html"
    #fields = "__all__"

class updateArticleView(UpdateView):
    model = Post
    form_class = updateForm
    template_name = "editBlog.html"

class addCategoryView(CreateView):
    model = Category
    template_name = "addCategory.html"
    fields = ['name']

class deleteArticleView(DeleteView):
    model = Post
    template_name = "deleteBlog.html"
    success_url = reverse_lazy("home")

class TagIndexView(ListView):
    model = Post
    template_name = 'tagsListView.html'
    paginate_by = 3
    #context_object_name = "obj"

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'),draft=False)

    def get_context_data(self, **kwargs):
        context = super(TagIndexView, self).get_context_data(**kwargs)
        context.update({"tag_name":self.kwargs.get('slug').title()})
        return context

class TagListView(ListView):
    model = Tag
    template_name = 'tagList.html'