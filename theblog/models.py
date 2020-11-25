from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse, reverse_lazy
from datetime import datetime,date

from ckeditor.fields import RichTextField

from django.db.models.signals import pre_save
from django.utils.text import slugify

from taggit.managers import TaggableManager

import readtime

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True,blank=True,upload_to="images/profile/")
    facebook_url = models.CharField(max_length=255,blank=True,null=True)
    twitter_url = models.CharField(max_length=255, blank=True,null=True)
    instagram_url = models.CharField(max_length=255, blank=True,null=True)

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title = models.CharField(max_length=255,default=" ")
    title_tag = models.CharField(max_length=255,default=" ")
    slug = models.SlugField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank=True,null=True)
    snippet = models.CharField(max_length=1000)
    image = models.ImageField(null=True,blank=True,upload_to="images/")
    draft = models.BooleanField(default=False)
    publish = models.DateTimeField(auto_now=False,auto_now_add=False)
    post_date = models.DateTimeField(auto_now_add=True)

    tags = TaggableManager()

    def __str__(self):
        return self.title + " | "+ str(self.author)

    def get_absolute_url(self):
        print(str(self.pk))
        return reverse('article-detail',kwargs={"slug":self.slug})

    def get_readtime(self):
        result = readtime.of_text(self.body)
        return result.text

#Signals.py

#Posts
def create_slug(instance,new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s"%(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver,sender=Post)


#Category
def create_slug_cat(instance,new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Category.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s"%(slug,qs.first().id)
        return create_slug_cat(instance,new_slug=new_slug)
    return slug

def pre_save_cat_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug_cat(instance)

pre_save.connect(pre_save_cat_receiver,sender=Category)