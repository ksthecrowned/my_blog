from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
  def get_queryset(self):
    return super(PublishedManager,
                  self).get_queryset()\
                       .filter(status='published')


class Author(models.Model):
  image = models.ImageField(upload_to='media')
  complete_name = models.CharField(max_length=100)
  email = models.EmailField()
  info = models.TextField(max_length=500)
  facebook = models.URLField(null=True, blank=True)
  twitter = models.URLField(null=True, blank=True)
  instagram = models.URLField(null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ('complete_name',)

  def __str__(self):
    return self.complete_name


class Post(models.Model):
  STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
  )
  title = models.CharField(max_length=250)
  slug = models.SlugField(max_length=250,
                          unique_for_date='publish')
  author = models.ForeignKey(Author,
                            on_delete=models.CASCADE,
                            related_name='blog_posts')
  body = models.TextField()
  cover = models.ImageField(upload_to='media')
  publish = models.DateTimeField(default=timezone.now)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  status = models.CharField(max_length=10,
                            choices=STATUS_CHOICES,
                            default='draft')

  objects = models.Manager() # The default manager.
  published = PublishedManager() # Our custom manager.
  tags = TaggableManager()

  def get_absolute_url(self):
    return reverse('blog:post_detail',
                    args=[self.publish.year,
                    self.publish.month,
                    self.publish.day, self.slug])

  class Meta:
    ordering = ('-publish',)

  def __str__(self):
    return self.title


class Comment(models.Model):
  post = models.ForeignKey(Post,
                           on_delete=models.CASCADE,
                           related_name='comments')
  name = models.CharField('Votre nom', max_length=80)
  email = models.EmailField()
  body = models.TextField('')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  class Meta:
    ordering = ('created',)

  def __str__(self):
    return f'Comment by {self.name} on {self.post}'
