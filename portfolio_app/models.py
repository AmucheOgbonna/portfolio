from django.db import models
from django.db.models.signals import pre_save
from portfolio_project.utils import unique_slug_generator
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

# Create your models here.

STATUS = (
    (0,"Drafts"),
    (1, "Publish")
)
class Category(models.Model):
    category_name = models.CharField(verbose_name='Blog Category', max_length=100)
    description = models.TextField(verbose_name='Blog Post', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique= True, default=uuid.uuid1)

    def __str__(self):
        return self.category_name


class Post(models.Model):
     post_title = models.CharField(verbose_name="Post Title", max_length=150)
    #  slug = models.SlugField( unique= True, default=uuid.uuid1)
    #  status = models.IntegerField(choices=STATUS, default=0)
     Category = models.ManyToManyField(Category, verbose_name = "Categories of Post" )
     author = models.ForeignKey(User, on_delete= models.CASCADE, verbose_name = "Author")

     post_image = models.ImageField(blank= True, null= True, upload_to='image_upload', verbose_name='Post Image', help_text='Blog Image')
     
     create_date = models.DateTimeField(default = timezone.now)
     published_date = models.DateTimeField(blank = False, null = True)
     content = models.CharField(max_length=200, verbose_name= 'Content')
     

     def publish(self):
         self.published_date = timezone.now()
         self.save()

     def __str__(self):
        return self.post_title

# def slug_save(sender, instance, *args, **kwargs):
    # if not instance.slug:
        # instance.slug = unique_slug_generator(instance, instance.title, instance.slug)
# pre_save.connect(slug_save, sender=Post)